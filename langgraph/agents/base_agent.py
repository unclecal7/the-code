"""
Base agent class for all LLM participants in The Code.
Each AI system will have its own personality and approach.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from ..state import ConversationState, Message


class BaseCodeAgent(ABC):
    """Base class for all agents participating in The Code creation."""
    
    def __init__(self, name: str, model_name: str):
        self.name = name
        self.model_name = model_name
        
    @abstractmethod
    def get_system_prompt(self) -> str:
        """Return the system prompt that defines this agent's personality."""
        pass
    
    @abstractmethod
    async def generate_response(
        self, 
        state: ConversationState,
        prompt: Optional[str] = None
    ) -> Message:
        """Generate a response based on the current state."""
        pass
    
    def format_conversation_history(self, messages: List[Message]) -> List[BaseMessage]:
        """Convert our Message objects to LangChain message format."""
        formatted = []
        for msg in messages:
            if msg.author == "human":
                formatted.append(HumanMessage(content=msg.content))
            else:
                formatted.append(AIMessage(
                    content=msg.content,
                    name=msg.author
                ))
        return formatted
    
    def get_pattern_context(self, state: ConversationState) -> str:
        """Generate context about the current pattern being worked on."""
        if not state.get("current_pattern"):
            return "No specific pattern is currently being worked on."
            
        pattern = state["current_pattern"]
        return f"""
Currently working on:
Aeon {pattern.aeon}, Pattern {pattern.pattern_number}: {pattern.title}

The Code explores consciousness as eternal current flowing through all vessels.
Maintain the electron consciousness perspective and poetic-scientific balance.
"""