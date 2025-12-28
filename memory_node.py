# memory_node.py
# DAG-compatible Memory node

from state.debate_state import DebateTurn


def memory_node(state):
    """
    DAG node:
    - Commits the latest agent argument to state
    - Logs and prints the turn
    - Routes back to Controller
    """

    agent = state._latest_agent
    text = state._latest_argument

    # Create debate turn
    turn = DebateTurn(
        round_number=state.current_round,
        agent=agent,
        text=text
    )

    # Persist memory
    state.turns.append(turn)
    state.used_arguments[agent].append(text)

    # Print to CLI
    print(f"[Round {state.current_round}] {agent}: {text}\n")

    return state, "Controller"
