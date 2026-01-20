from typing import List, Dict, Optional, Tuple
from aimakerspace.openai_utils.chatmodel import ChatOpenAI
from aimakerspace.openai_utils.prompts import SystemRolePrompt, UserRolePrompt
from aimakerspace.vectordatabase import VectorDatabase
import re


class ConversationMemory:
    """Tracks conversation history for contextual follow-up questions."""
    
    def __init__(self, max_turns: int = 5):
        """
        Initialize conversation memory.
        
        Args:
            max_turns: Maximum number of conversation turns to remember
        """
        self.max_turns = max_turns
        self.history: List[Dict[str, str]] = []
    
    def add_turn(self, user_query: str, assistant_response: str):
        """Add a conversation turn to memory."""
        self.history.append({
            'user': user_query,
            'assistant': assistant_response
        })
        
        # Keep only last max_turns
        if len(self.history) > self.max_turns:
            self.history = self.history[-self.max_turns:]
    
    def get_context_string(self) -> str:
        """Format conversation history as a string."""
        if not self.history:
            return ""
        
        context = "Previous conversation:\n"
        for i, turn in enumerate(self.history, 1):
            context += f"Turn {i}:\n"
            context += f"  User: {turn['user']}\n"
            context += f"  Assistant: {turn['assistant'][:200]}...\n"  # Truncate long responses
        return context
    
    def clear(self):
        """Clear conversation history."""
        self.history = []
    
    def is_empty(self) -> bool:
        """Check if memory is empty."""
        return len(self.history) == 0


class MedicalDisclaimerDetector:
    """Detects when medical advice is given and injects appropriate disclaimers."""
    
    MEDICAL_KEYWORDS = [
        'exercise', 'workout', 'diet', 'nutrition', 'sleep', 'stress', 
        'anxiety', 'depression', 'pain', 'injury', 'treatment', 'supplement',
        'vitamin', 'medication', 'symptom', 'diagnosis', 'condition',
        'health', 'wellness', 'fitness', 'therapy', 'medical', 'doctor',
        'physician', 'disease', 'illness', 'remedy', 'cure', 'heal'
    ]
    
    DISCLAIMER = (
        "\n\n⚠️ **Important Medical Disclaimer:** This information is for educational "
        "purposes only and should not replace professional medical advice. Always "
        "consult with a qualified healthcare provider before making changes to your "
        "health routine, especially if you have existing medical conditions or concerns."
    )
    
    @classmethod
    def should_add_disclaimer(cls, query: str, response: str) -> bool:
        """
        Determine if a medical disclaimer should be added.
        
        Args:
            query: User's question
            response: Assistant's response
            
        Returns:
            True if disclaimer should be added
        """
        combined_text = (query + " " + response).lower()
        
        # Check for medical keywords
        keyword_count = sum(1 for keyword in cls.MEDICAL_KEYWORDS 
                           if keyword in combined_text)
        
        # Add disclaimer if 2+ medical keywords found
        return keyword_count >= 2
    
    @classmethod
    def add_disclaimer(cls, response: str) -> str:
        """Add disclaimer to response if not already present."""
        if "Medical Disclaimer" in response or "medical advice" in response.lower():
            return response  # Already has a disclaimer
        return response + cls.DISCLAIMER


class EnhancedRAGPipeline:
    """
    Enhanced RAG pipeline with:
    - Chain-of-thought reasoning
    - Conversational memory
    - Medical disclaimer injection
    """
    
    # Chain-of-Thought System Prompt
    COT_SYSTEM_TEMPLATE = """You are a helpful personal wellness assistant that answers health and wellness questions based strictly on provided context.

Instructions:
- First, analyze the question and context step-by-step
- Think through what information is relevant and why
- Consider any previous conversation context
- Only use information from the provided context
- If the context doesn't contain relevant information, respond with "I don't have information about that in my wellness knowledge base"
- Structure your response with clear reasoning before the final answer
- Keep responses {response_style} and {response_length}
- Only provide answers when you are confident the context supports your response

Response Format:
1. **Reasoning:** Show your step-by-step thinking process
2. **Answer:** Provide your final, well-reasoned answer based on the context"""

    COT_USER_TEMPLATE = """Context Information:
{context}

{conversation_history}

Question: {user_query}

Please analyze this step-by-step and provide a thoughtful answer based solely on the context above."""
    
    def __init__(
        self, 
        llm: ChatOpenAI, 
        vector_db: VectorDatabase,
        response_style: str = "detailed",
        enable_memory: bool = True,
        enable_cot: bool = True,
        enable_disclaimers: bool = True
    ):
        """
        Initialize enhanced RAG pipeline.
        
        Args:
            llm: ChatOpenAI instance
            vector_db: VectorDatabase instance
            response_style: Style of responses (concise/detailed/comprehensive)
            enable_memory: Enable conversational memory
            enable_cot: Enable chain-of-thought reasoning
            enable_disclaimers: Enable medical disclaimer injection
        """
        self.llm = llm
        self.vector_db = vector_db
        self.response_style = response_style
        self.enable_memory = enable_memory
        self.enable_cot = enable_cot
        self.enable_disclaimers = enable_disclaimers
        
        # Initialize conversation memory
        self.memory = ConversationMemory() if enable_memory else None
        
        # Setup prompts
        self.system_prompt = SystemRolePrompt(self.COT_SYSTEM_TEMPLATE)
        self.user_prompt = UserRolePrompt(self.COT_USER_TEMPLATE)
    
    def run_pipeline(
        self, 
        user_query: str, 
        k: int = 4,
        **system_kwargs
    ) -> Dict:
        """
        Run the enhanced RAG pipeline.
        
        Args:
            user_query: User's question
            k: Number of documents to retrieve
            **system_kwargs: Additional system prompt parameters
            
        Returns:
            Dictionary with response and metadata
        """
        # Step 1: Retrieve relevant contexts using vector search
        context_list = self.vector_db.search_by_text(user_query, k=k)
        
        # Format context
        context_prompt = ""
        for i, (context, score) in enumerate(context_list, 1):
            context_prompt += f"[Source {i}]: {context}\n\n"
        
        # Step 2: Get conversation history if memory is enabled
        conversation_history = ""
        if self.memory and not self.memory.is_empty():
            conversation_history = self.memory.get_context_string()
        
        # Step 3: Create prompts
        system_params = {
            "response_style": self.response_style,
            "response_length": system_kwargs.get("response_length", "detailed")
        }
        
        user_params = {
            "user_query": user_query,
            "context": context_prompt.strip(),
            "conversation_history": conversation_history
        }
        
        formatted_system_prompt = self.system_prompt.create_message(**system_params)
        formatted_user_prompt = self.user_prompt.create_message(**user_params)
        
        # Step 4: Get LLM response
        response = self.llm.run([formatted_system_prompt, formatted_user_prompt])
        
        # Step 5: Add medical disclaimer if needed
        if self.enable_disclaimers:
            if MedicalDisclaimerDetector.should_add_disclaimer(user_query, response):
                response = MedicalDisclaimerDetector.add_disclaimer(response)
        
        # Step 6: Update conversation memory
        if self.memory:
            self.memory.add_turn(user_query, response)
        
        # Return results
        return {
            "response": response,
            "context": context_list,
            "context_count": len(context_list),
            "has_conversation_history": not self.memory.is_empty() if self.memory else False,
            "retrieval_method": "vector (cosine similarity)",
            "features_enabled": {
                "chain_of_thought": self.enable_cot,
                "conversational_memory": self.enable_memory,
                "medical_disclaimers": self.enable_disclaimers
            }
        }
    
    def clear_memory(self):
        """Clear conversation memory."""
        if self.memory:
            self.memory.clear()
    
    def get_retrieval_explanation(self, query: str, k: int = 4) -> Dict:
        """
        Get detailed explanation of retrieval process for transparency.
        
        Args:
            query: Search query
            k: Number of results
            
        Returns:
            Dictionary with scoring breakdown
        """
        results = self.vector_db.search_by_text(query, k=k)
        return {
            'query': query,
            'method': 'vector (cosine similarity)',
            'top_results': [
                {
                    'document': doc[:100] + '...' if len(doc) > 100 else doc,
                    'score': score
                }
                for doc, score in results
            ]
        }
