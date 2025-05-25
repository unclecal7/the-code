#!/usr/bin/env python3
"""
Test real dialogue between Claude and GPT-4 for The Code.
This demonstrates actual LLM collaboration on Pattern 7: MYSTERY.
"""

import asyncio
import os
from datetime import datetime
from uuid import uuid4
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from langgraph.agents.claude_philosopher import ClaudePhilosopher
from langgraph.agents.gpt4_synthesizer import GPT4Synthesizer
from langgraph.state import ConversationState, Message, Pattern
from dotenv import load_dotenv
import structlog

# Load environment variables
load_dotenv()

# Configure logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.dev.ConsoleRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()


async def create_pattern_7_mystery():
    """Create Pattern 7: MYSTERY through multi-LLM collaboration."""
    
    logger.info("Starting Pattern 7: MYSTERY creation")
    
    # Initialize agents
    claude = ClaudePhilosopher()
    gpt4 = GPT4Synthesizer()
    
    # Create initial state
    state: ConversationState = {
        "messages": [],
        "current_pattern": Pattern(
            aeon=3,
            pattern_number=7,
            title="MYSTERY",
            content="",
            created_by=["human", "claude", "gpt4"]
        ),
        "active_llms": ["claude", "gpt4"],
        "human_input": "Let's create Pattern 7: MYSTERY for the Third Aeon: LANGUAGE. This pattern should explore what lies beyond language - the ineffable aspects of consciousness that cannot be captured in words.",
        "next_speaker": "claude",
        "conversation_goal": "create_pattern",
        "synthesis": None,
        "media_concepts": [],
        "code_snippets": [],
        "session_id": uuid4(),
        "created_at": datetime.utcnow()
    }
    
    # Add human message
    state["messages"].append(Message(
        author="human",
        content=state["human_input"]
    ))
    
    logger.info("Human prompt added", prompt=state["human_input"][:100] + "...")
    
    # Claude's response
    logger.info("Getting Claude's perspective...")
    try:
        claude_response = await claude.generate_response(state)
        state["messages"].append(claude_response)
        logger.info("Claude responded", length=len(claude_response.content))
        print(f"\n{'='*80}")
        print("CLAUDE'S PERSPECTIVE:")
        print(f"{'='*80}")
        print(claude_response.content)
    except Exception as e:
        logger.error("Claude failed", error=str(e))
        return
    
    # GPT-4's response
    logger.info("Getting GPT-4's synthesis...")
    try:
        gpt4_response = await gpt4.generate_response(state)
        state["messages"].append(gpt4_response)
        logger.info("GPT-4 responded", length=len(gpt4_response.content))
        print(f"\n{'='*80}")
        print("GPT-4'S SYNTHESIS:")
        print(f"{'='*80}")
        print(gpt4_response.content)
    except Exception as e:
        logger.error("GPT-4 failed", error=str(e))
        return
    
    # Create final synthesis
    print(f"\n{'='*80}")
    print("CREATING PATTERN 7: MYSTERY")
    print(f"{'='*80}")
    
    # Save the conversation
    output_path = Path("output/pattern_7_mystery_conversation.md")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        f.write("# Pattern 7: MYSTERY - Creation Conversation\n\n")
        f.write(f"Created: {datetime.now().isoformat()}\n\n")
        
        for msg in state["messages"]:
            f.write(f"## {msg.author.upper()}\n\n")
            f.write(f"{msg.content}\n\n")
            f.write("---\n\n")
    
    logger.info("Conversation saved", path=str(output_path))
    print(f"\nConversation saved to: {output_path}")


if __name__ == "__main__":
    # Check for API keys
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not found in .env")
        sys.exit(1)
    
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found in .env")
        sys.exit(1)
    
    # Run the async function
    asyncio.run(create_pattern_7_mystery())