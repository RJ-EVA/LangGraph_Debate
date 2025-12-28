# generate_dag.py
# Generates DAG diagram for the debate workflow

from graphviz import Digraph


def generate_dag():
    dot = Digraph(
        comment="Multi-Agent Debate DAG",
        format="png"
    )

    # Nodes
    dot.node("UserInput", "UserInputNode\n(CLI Topic Input)")
    dot.node("Controller", "ControllerNode\n(Round & Turn Router)")
    dot.node("AgentA", "AgentA\n(Scientist)")
    dot.node("AgentB", "AgentB\n(Philosopher)")
    dot.node("Memory", "MemoryNode\n(Commit + Log)")
    dot.node("Judge", "JudgeNode\n(Evaluation)")
    dot.node("END", "END")

    # Edges
    dot.edge("UserInput", "Controller")
    dot.edge("Controller", "AgentA", label="Odd Round")
    dot.edge("Controller", "AgentB", label="Even Round")
    dot.edge("AgentA", "Memory")
    dot.edge("AgentB", "Memory")
    dot.edge("Memory", "Controller")
    dot.edge("Controller", "Judge", label="After 8 Rounds")
    dot.edge("Judge", "END")

    # Render diagram
    dot.render("dag")


if __name__ == "__main__":
    generate_dag()
