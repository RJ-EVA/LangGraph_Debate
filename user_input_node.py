# user_input_node.py
# DAG-compatible UserInput node

from state.debate_state import DebateState


def user_input_node(state):
    """
    DAG node:
    - Prompts user for debate topic
    - Stores topic in state
    - Routes to Controller node
    """

    topic = input("Enter topic for debate: ").strip()

    if not topic:
        raise ValueError("Debate topic cannot be empty.")

    if len(topic) < 10:
        raise ValueError("Debate topic must be at least 10 characters long.")

    state.topic = topic

    return state, "Controller"
