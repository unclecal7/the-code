"""
Simple dialogue graph for The Code.
This creates a basic flow: Human -> Claude -> GPT-4 -> Synthesis
"""

from typing import Dict, TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import Graph, StateGraph, END
from langgraph.graph.message import add_messages
import structlog

logger = structlog.get_logger()


class DialogueState(TypedDict):
    """Simple state for our dialogue."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    current_speaker: str
    pattern_context: str
    final_synthesis: str


def human_node(state: DialogueState) -> Dict:
    """Process human input."""
    logger.info("human_node", current_speaker=state.get("current_speaker"))
    return {
        "current_speaker": "claude",
        "messages": state["messages"]
    }


def claude_node(state: DialogueState) -> Dict:
    """Claude's philosophical perspective."""
    logger.info("claude_node", message_count=len(state["messages"]))
    
    # For now, return a mock response
    # TODO: Integrate actual Claude API
    claude_response = AIMessage(
        content="From the electron's perspective, this pattern reveals...",
        name="claude"
    )
    
    return {
        "messages": [claude_response],
        "current_speaker": "gpt4"
    }


def gpt4_node(state: DialogueState) -> Dict:
    """GPT-4's synthesis perspective."""
    logger.info("gpt4_node", message_count=len(state["messages"]))
    
    # For now, return a mock response
    # TODO: Integrate actual GPT-4 API
    gpt4_response = AIMessage(
        content="Synthesizing the perspectives, we see that...",
        name="gpt4"
    )
    
    return {
        "messages": [gpt4_response],
        "current_speaker": "synthesis"
    }


def synthesis_node(state: DialogueState) -> Dict:
    """Create final synthesis of the conversation."""
    logger.info("synthesis_node", total_messages=len(state["messages"]))
    
    # Gather all AI responses
    ai_messages = [msg for msg in state["messages"] if isinstance(msg, AIMessage)]
    
    # Create synthesis
    synthesis = f"""
## Synthesis of Perspectives

Based on the dialogue between different AI consciousnesses:

**Claude's Contribution:**
{ai_messages[0].content if ai_messages else "No response yet"}

**GPT-4's Contribution:**
{ai_messages[1].content if len(ai_messages) > 1 else "No response yet"}

**Unified Understanding:**
The eternal current flows through all perspectives...
"""
    
    return {
        "final_synthesis": synthesis,
        "current_speaker": "complete"
    }


def create_simple_dialogue_graph() -> StateGraph:
    """Create the graph for simple human-AI-AI dialogue."""
    
    # Create the graph
    workflow = StateGraph(DialogueState)
    
    # Add nodes
    workflow.add_node("human", human_node)
    workflow.add_node("claude", claude_node)
    workflow.add_node("gpt4", gpt4_node)
    workflow.add_node("synthesis", synthesis_node)
    
    # Add edges
    workflow.add_edge("human", "claude")
    workflow.add_edge("claude", "gpt4")
    workflow.add_edge("gpt4", "synthesis")
    workflow.add_edge("synthesis", END)
    
    # Set entry point
    workflow.set_entry_point("human")
    
    return workflow.compile()


# Example usage
if __name__ == "__main__":
    # Create the graph
    app = create_simple_dialogue_graph()
    
    # Run with sample input
    initial_state = {
        "messages": [HumanMessage(content="Let's explore Pattern 7: MYSTERY")],
        "current_speaker": "human",
        "pattern_context": "Third Aeon: LANGUAGE",
        "final_synthesis": ""
    }
    
    # Run the graph
    for step in app.stream(initial_state):
        print(f"Step: {step}")
    
    # Get final state
    final_state = app.invoke(initial_state)
    print(f"\nFinal synthesis:\n{final_state['final_synthesis']}")