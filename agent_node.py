# agent_node.py
# DAG-compatible Agent nodes

from nodes.memory_utils import get_relevant_memory

from nodes.agent_logic import generate_argument  # we will create this helper next


def agent_a_node(state):
    """
    DAG node for AgentA (Scientist)
    """
    # Increment round
    state.current_round += 1

    # Get relevant memory slice
    memory = get_relevant_memory(state, "AgentA")

    # Generate argument
    argument = generate_argument("AgentA", memory)

    # Temporarily store argument in state
    state._latest_agent = "AgentA"
    state._latest_argument = argument

    return state, "Memory"


def agent_b_node(state):
    """
    DAG node for AgentB (Philosopher)
    """
    # Increment round
    state.current_round += 1

    # Get relevant memory slice
    memory = get_relevant_memory(state, "AgentB")

    # Generate argument
    argument = generate_argument("AgentB", memory)

    # Temporarily store argument in state
    state._latest_agent = "AgentB"
    state._latest_argument = argument

    return state, "Memory"
