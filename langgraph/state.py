"""
State management for The Code LangGraph implementation.
Defines the shared state that flows through our multi-LLM conversations.
"""

from typing import TypedDict, List, Dict, Optional, Literal
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Message(BaseModel):
    """A single message in a conversation."""
    id: UUID = Field(default_factory=uuid4)
    author: str  # 'human', 'claude', 'gpt4', 'gemini', etc.
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict = Field(default_factory=dict)


class Pattern(BaseModel):
    """A single pattern in The Code."""
    aeon: int
    pattern_number: int
    title: str
    content: str
    created_by: List[str]  # Can have multiple authors!
    version: int = 1
    parent_version: Optional[UUID] = None
    media_links: Dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    

class ConversationState(TypedDict):
    """State that flows through LangGraph nodes."""
    # Current conversation
    messages: List[Message]
    current_pattern: Optional[Pattern]
    
    # Participants in this conversation
    active_llms: List[str]
    human_input: Optional[str]
    
    # Control flow
    next_speaker: Optional[str]
    conversation_goal: str  # 'create_pattern', 'discuss_theme', 'multimedia_design', etc.
    
    # Output accumulation
    synthesis: Optional[str]
    media_concepts: List[Dict]
    code_snippets: List[str]
    
    # Metadata
    session_id: UUID
    created_at: datetime