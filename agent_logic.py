# agent_logic.py
# Core agent argument generation logic (LLM placeholder)

def generate_argument(agent_name, memory):
    topic = memory["topic"]
    last_opponent_argument = memory["last_opponent_argument"]
    own_arguments = memory["own_arguments"]

    base = f"{agent_name} argues on '{topic}' from their perspective."

    if base in own_arguments:
        base = f"{agent_name} adds a new supporting point on '{topic}'."

    if last_opponent_argument:
        base += " Responding to the opponent's previous argument."

    return base
