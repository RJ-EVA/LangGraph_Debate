# judge_node.py
# DAG-compatible Judge node

def judge_node(state):
    """
    DAG terminal node:
    - Reviews the full debate
    - Declares a winner
    - Ends execution
    """

    # Build debate summary
    summary_lines = []
    for turn in state.turns:
        summary_lines.append(
            f"Round {turn.round_number} - {turn.agent}: {turn.text}"
        )

    summary = "\n".join(summary_lines)

    # Simple evaluation logic (deterministic placeholder)
    a_count = len(state.used_arguments["AgentA"])
    b_count = len(state.used_arguments["AgentB"])

    if a_count > b_count:
        winner = "AgentA"
        reason = "Presented more structured, risk-aware, and consistent arguments."
    else:
        winner = "AgentB"
        reason = "Demonstrated stronger philosophical reasoning and abstraction."

    # Print verdict
    print("=== JUDGE SUMMARY ===")
    print(summary)
    print("\nWinner:", winner)
    print("Reason:", reason)

    # Store verdict in state for logging
    state.judge_verdict = {
        "summary": summary,
        "winner": winner,
        "reason": reason
    }

    return state, "END"
