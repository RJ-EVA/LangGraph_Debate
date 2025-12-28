# memory_utils.py
# Helper functions for memory access (non-DAG)

def get_relevant_memory(state, agent):
    """
    Provide agent-specific memory slice.
    """
    opponent = "AgentB" if agent == "AgentA" else "AgentA"

    last_opponent_argument = None
    for turn in reversed(state.turns):
        if turn.agent == opponent:
            last_opponent_argument = turn.text
            break

    return {
        "topic": state.topic,
        "last_opponent_argument": last_opponent_argument,
        "own_arguments": state.used_arguments[agent]
    }
