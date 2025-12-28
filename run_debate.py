# run_debate.py
# DAG-based CLI runner (LangGraph-compatible)

from state.debate_state import DebateState
from nodes.user_input_node import user_input_node
from nodes.controller_node import controller_node
from nodes.agent_node import agent_a_node, agent_b_node
from nodes.memory_node import memory_node
from nodes.judge_node import judge_node
from nodes.logger_node import Logger
from dag_executor import DAGExecutor


def main():
    # Initialize empty state
    state = DebateState(topic="")

    # Initialize logger
    logger = Logger("logs/debate_log.json")

    # Register DAG nodes
    nodes = {
        "UserInput": user_input_node,
        "Controller": controller_node,
        "AgentA": agent_a_node,
        "AgentB": agent_b_node,
        "Memory": memory_node,
        "Judge": judge_node
    }

    # Create DAG executor
    dag = DAGExecutor(
        nodes=nodes,
        entry_node="UserInput",
        logger=logger
    )

    # Run DAG
    dag.run(state)


if __name__ == "__main__":
    main()
