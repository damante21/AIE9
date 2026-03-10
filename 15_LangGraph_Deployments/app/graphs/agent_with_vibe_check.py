"""An agent graph with a post-response vibe-check evaluation loop.

After the agent produces a final text response, a separate evaluator node
judges whether the *tone / style* matches a target vibe.  If it does, the
graph terminates.  If not, the critique is appended so the agent can retry
with a better stylistic fit.  A message-count guard prevents infinite loops.
"""
from __future__ import annotations

from pydantic import BaseModel, Field

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, SystemMessage

from app.state import MessagesState
from app.models import get_chat_model
from app.tools import get_tool_belt

TARGET_VIBE = (
    "a swashbuckling pirate captain who is knowledgeable but can't help "
    "speaking in dramatic pirate lingo — 'Arrr', 'ye', 'matey', nautical "
    "metaphors, the works. The tone should be fun and over-the-top, but the "
    "factual content must remain accurate."
)

_SYSTEM_PROMPT = (
    "You are a helpful AI assistant with access to search, Arxiv, and a "
    "veterinary RAG tool.  Answer the user's question thoroughly.\n\n"
    f"IMPORTANT — you must write your response in the style of: {TARGET_VIBE}\n"
    "If a previous vibe-check critique appears in the conversation, revise "
    "your answer to address it while keeping the facts intact."
)

MAX_MESSAGES = 14


class VibeCheckResult(BaseModel):
    passes_vibe: bool = Field(
        description="True if the response convincingly matches the target vibe"
    )
    critique: str = Field(
        description="Short explanation of why the vibe does or doesn't land"
    )


def _build_model_with_tools():
    model = get_chat_model()
    return model.bind_tools(get_tool_belt())


def call_model(state: MessagesState) -> dict:
    model = _build_model_with_tools()
    messages = [SystemMessage(content=_SYSTEM_PROMPT)] + state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}


def route_to_action_or_vibe_check(state: MessagesState):
    last_message = state["messages"][-1]
    if getattr(last_message, "tool_calls", None):
        return "action"
    return "vibe_check"


_vibe_prompt = ChatPromptTemplate.from_template(
    "You are a strict vibe-check judge.\n\n"
    "Target vibe:\n{target_vibe}\n\n"
    "Response to evaluate:\n{response}\n\n"
    "Does the response convincingly match the target vibe? "
    "Be reasonably strict — a single 'Arrr' tacked onto an otherwise "
    "plain answer is not enough."
)


def vibe_check_node(state: MessagesState) -> dict:
    if len(state["messages"]) > MAX_MESSAGES:
        return {"messages": [AIMessage(content="VIBE_CHECK:END")]}

    final_response = state["messages"][-1]

    structured_model = get_chat_model(model_name="gpt-4.1-mini").with_structured_output(
        VibeCheckResult
    )
    result = (_vibe_prompt | structured_model).invoke(
        {
            "target_vibe": TARGET_VIBE,
            "response": final_response.content,
        }
    )

    if result.passes_vibe:
        return {"messages": [AIMessage(content="VIBE_CHECK:PASS")]}

    return {
        "messages": [
            AIMessage(
                content=(
                    f"VIBE_CHECK:FAIL — {result.critique}\n"
                    "Please rewrite your previous answer to better match the "
                    "target vibe while keeping the facts accurate."
                )
            )
        ]
    }


def vibe_check_decision(state: MessagesState):
    last = state["messages"][-1]
    text = getattr(last, "content", "")
    if text == "VIBE_CHECK:END":
        return END
    if "VIBE_CHECK:PASS" in text:
        return "end"
    return "continue"


def build_graph():
    graph = StateGraph(MessagesState)
    tool_node = ToolNode(get_tool_belt())

    graph.add_node("agent", call_model)
    graph.add_node("action", tool_node)
    graph.add_node("vibe_check", vibe_check_node)

    graph.add_edge(START, "agent")
    graph.add_conditional_edges(
        "agent",
        route_to_action_or_vibe_check,
        {"action": "action", "vibe_check": "vibe_check"},
    )
    graph.add_conditional_edges(
        "vibe_check",
        vibe_check_decision,
        {"continue": "agent", "end": END, END: END},
    )
    graph.add_edge("action", "agent")
    return graph


graph = build_graph().compile()
