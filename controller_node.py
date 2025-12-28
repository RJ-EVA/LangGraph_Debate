# controller_node.py
# DAG router node that enforces rounds and turn order

MAX_ROUNDS = 8


def controller_node(state):
    """
    DAG node:
    - Decides whether debate continues or ends
    - Routes to AgentA, AgentB, or Judge
    """

    # If max rounds reached, go to Judge
    if state.current_round >= MAX_ROUNDS:
        return state, "Judge"

    # Decide next agent based on round number
    next_round = state.current_round + 1

    if next_round % 2 == 1:
        return state, "AgentA"
    else:
        return state, "AgentB"
