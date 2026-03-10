<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Session 15: Build & Serve Agentic Graphs with LangGraph</h1>

| 📰 Session Sheet                                             | ⏺️ Recording                           | 🖼️ Slides                                  | 👨‍💻 Repo    | 📝 Homework                                      | 📁 Feedback                                          |
| ------------------------------------------------------------ | -------------------------------------- | ------------------------------------------- | ------------- | ------------------------------------------------ | ---------------------------------------------------- |
| [Agent Servers](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Session_Sheets/15_Agent_Servers) |[Recording!](https://us02web.zoom.us/rec/share/lORjByDju6fv4TdE3r93dorY3aNgmSKL_Qk_cX_AMcCQ6cNfSW77unaA1LMVV60.OcI8uEnfVmRAgjSn) <br> passcode: `Dc@&pv1T`| [Session 15 Slides](https://www.canva.com/design/DAG-EJqkRaM/FR3WG_yMA5_BqbWpQlHR9g/edit?utm_content=DAG-EJqkRaM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 15 Assignment: Agent Servers](https://forms.gle/Vb3HNDsyVPQ1jqKX7) | [Feedback 3/3](https://forms.gle/kYmhbVUEMog16mKv8) |

### Prerequisites

Before starting, ensure you have the following:

- **Python 3.11+** installed
- An **OpenAI API Key**
- A **Tavily API Key**
- (Optional) **LangSmith** credentials for tracing

Create a `.env` file in this directory with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```
2. Run `uv sync` to install dependencies.

# Build 🏗️

Run the repository and complete the following:

- 🤝 Breakout Room Part #1 — Building and serving your LangGraph Agent Graph
  - Task 1: Getting Dependencies & Environment
    - Configure `.env` (OpenAI, Tavily, optional LangSmith)
  - Task 2: Serve the Graph Locally
    - `uv run langgraph dev` (API on http://localhost:2024)
  - Task 3: Call the API from a different terminal
    - `uv run test_served_graph.py` (sync SDK example)
  - Task 4: Explore assistants (from `langgraph.json`)
    - `agent` → `simple_agent` (tool-using agent)
    - `agent_helpful` → `agent_with_helpfulness` (separate helpfulness node)

- 🤝 Breakout Room Part #2 — Using LangSmith Studio to visualize the graph
  - Task 1: Open Studio while the server is running
    - https://smith.langchain.com/studio?baseUrl=http://localhost:2024
  - Task 2: Visualize & Stream
    - Start a run and observe node-by-node updates
  - Task 3: Compare Flows
    - Contrast `agent` vs `agent_helpful` (tool calls vs helpfulness decision)

<details>
<summary>🚧 Advanced Build 🚧 (OPTIONAL - <i>open this section for the requirements</i>)</summary>

>NOTE: This can be done in place of the Main Assignment

- Create and deploy a locally hosted MCP server with FastMCP.
- Extend your tools in `tools.py` to allow your LangGraph to consume the MCP Server.

When submitting, provide:
- Your Loom video link demonstrating the MCP server integration
- The GitHub URL to your completed Advanced Build

Have fun!
</details>

### Questions & Activities

#### Question 1:
What is the key architectural difference between the `simple_agent` and `agent_with_helpfulness` graphs? Specifically, explain how the helpfulness evaluation loop works and what mechanisms are in place to prevent it from running indefinitely.

##### Answer:

simple_agent is a standard ReAct loop: agent → (tool calls?) → action → agent → ... → END. It terminates as soon as the model responds without requesting tool calls.

agent_with_helpfulness adds a quality gate after the agent's final response. Instead of routing directly to END when there are no tool calls, it routes to a helpfulness evaluator node. If the response isn't deemed helpful enough, it loops back to the agent for another attempt.

The Helpfulness Evaluation Loop
Routing divergence — route_to_action_or_helpfulness replaces the prebuilt tools_condition. When the model's last message has no tool_calls, it routes to the helpfulness node instead of END.

Evaluation — helpfulness_node uses a separate model call (gpt-4.1-mini with structured output via HelpfulnessResult) to judge whether the response is "extremely helpful" relative to the original user query. It emits HELPFULNESS:Y or HELPFULNESS:N.

Decision — helpfulness_decision reads the verdict:

Y → route to END (response is good enough)
N → route back to agent (try again)
END marker → route to END (safety limit hit)
Infinite Loop Prevention
Two mechanisms:

Message count guard — Inside helpfulness_node, if len(state["messages"]) > 10, it short-circuits by emitting HELPFULNESS:END instead of calling the evaluator LLM. The helpfulness_decision function recognizes this sentinel and routes to END.

LangGraph's built-in recursion limit — The compiled graph has a default recursion limit (typically 25 steps) that will halt execution if the explicit guard somehow fails.

The message-count threshold of 10 is the primary safeguard, ensuring the loop can execute at most a few iterations before forcibly terminating regardless of the evaluator's judgment.


#### Question 2:
What is the role of `langgraph.json` in the LangGraph Deployments? Describe each of its key fields and how the platform uses this file to discover and serve your graphs.

##### Answer:

`langgraph.json` is the deployment manifest — it tells the LangGraph platform everything it needs to bootstrap, discover, and serve your agent graphs. The platform reads this file on startup (e.g. `uv run langgraph dev`) and uses it to configure the runtime.

**Key fields:**

- **`version`** (`1`) — Schema version of the manifest format. Ensures the platform parses the file correctly as the spec evolves.

- **`dependencies`** (`["."]`) — Python packages to install. `"."` means "install the current directory as a package" (i.e. run the equivalent of `pip install -e .`), which makes the `app` module importable.

- **`env`** (`".env"`) — Path to the environment variables file. The platform loads these (API keys, model names, LangSmith config) into the process environment before any graph code runs.

- **`python_version`** (`"3.13"`) — Specifies the Python runtime version for the deployment container/environment.

- **`graphs`** — A mapping of **graph ID → Python import path**. Each value uses `module.path:attribute` syntax (e.g. `"app.graphs.simple_agent:graph"`). The platform imports each module and grabs the compiled `graph` object, registering it under the given ID. These IDs become the API endpoints (e.g. `/threads/{id}/runs` with `graph_id=simple_agent`).

- **`assistants`** — A mapping of **assistant ID → configuration**. Each assistant references a `graph_id` from the `graphs` map and adds a human-readable `name` and `description`. Assistants are a higher-level abstraction — they let you create multiple named configurations (potentially with different default parameters) on top of the same underlying graph. The platform exposes these via the assistants API so clients can list and invoke them by name.

In short, `langgraph.json` is the single entry point the platform uses to resolve dependencies, load secrets, discover graph objects, and register named assistants — without it, the platform wouldn't know what to serve.

#### Activity #1:
Create your own agent graph! Build a new graph in `app/graphs/` with a custom evaluation node (e.g., a vibe checker, a fact verifier, a summarizer — get creative!). Register it in `langgraph.json`, serve it with `uv run langgraph dev`

##### Answer:

Created `app/graphs/agent_with_vibe_check.py` — a **Pirate Vibe Check Agent**.

**How it works:**
- The agent answers the user's question using the same tool belt (Tavily, Arxiv, RAG), but is system-prompted to respond in swashbuckling pirate style.
- After the agent produces a text response (no more tool calls), the graph routes to a `vibe_check` node instead of `END`.
- The `vibe_check` node uses `gpt-4.1-mini` with structured output (`VibeCheckResult`) to judge whether the response convincingly matches the pirate vibe. It returns a `passes_vibe` boolean and a `critique`.
- If the vibe passes → `END`. If it fails → the critique is appended to messages and the graph loops back to the agent for a rewrite.
- Safety: if `len(messages) > 14`, the vibe check short-circuits with `VIBE_CHECK:END` to prevent infinite loops.

**Graph topology:** `START` → `agent` → (tool calls? → `action` → `agent`) or → `vibe_check` → (PASS → `END`) or (FAIL → `agent`)

Registered in `langgraph.json` as `agent_with_vibe_check` with assistant ID `agent_vibes`.

# Ship 🚢

- The completed notebook.
- 5min. Loom Video

# Share 🚀

- Walk through your notebook and explain what you've completed in the Loom video
- Make a social media post about your final application and tag @AIMakerspace
- Share 3 lessons learned
- Share 3 lessons not learned

# Submitting Your Homework

### Main Homework Assignment

Follow these steps to prepare and submit your homework:

1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - _(You should have completed this process already.)_ For your initial repo setup, see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `15_LangGraph_Platform` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Answer Questions 1 - 2 using the `##### Answer:` markdown cell below them in the README
4. Complete Activity #1 in the README
5. Add, commit and push your modified files to your GitHub repository.

When submitting your homework, provide:
- Your Loom video link
- The GitHub URL to the `15_LangGraph_Platform` folder on your assignment branch
