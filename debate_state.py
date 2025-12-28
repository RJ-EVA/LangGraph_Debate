# debate_state.py
# Python 3.8 compatible

from typing import List, Dict
from dataclasses import dataclass, field


@dataclass
class DebateTurn:
    """
    Represents ONE turn in the debate.
    """
    round_number: int
    agent: str
    text: str


@dataclass
class DebateState:
    """
    Represents the ENTIRE debate state.
    This object is passed between nodes.
    """

    # Debate topic entered by the user
    topic: str

    # Current round number (1 to 8)
    current_round: int = 0

    # Whose turn it is: "AgentA" or "AgentB"
    current_agent: str = "AgentA"

    # Full list of debate turns
    turns: List[DebateTurn] = field(default_factory=list)

    # Used arguments to prevent repetition
    used_arguments: Dict[str, List[str]] = field(
        default_factory=lambda: {
            "AgentA": [],
            "AgentB": []
        }
    )

    # Any rule violations or errors
    errors: List[str] = field(default_factory=list)
