# dag_executor.py
# A minimal LangGraph-compatible DAG executor (Python 3.8 safe)

class DAGExecutor:
    def __init__(self, nodes, entry_node, logger):
        """
        nodes: dict of {node_name: node_function}
        entry_node: name of the starting node
        logger: Logger instance
        """
        self.nodes = nodes
        self.entry_node = entry_node
        self.logger = logger

    def run(self, state):
        """
        Execute the DAG until END is reached.
        """
        current_node = self.entry_node

        while current_node != "END":
            if current_node not in self.nodes:
                raise ValueError("Unknown node: " + current_node)

            self.logger.log("node_start", {"node": current_node})

            node_fn = self.nodes[current_node]

            state, next_node = node_fn(state)

            self.logger.log("node_end", {
                "node": current_node,
                "next_node": next_node,
                "round": state.current_round
            })

            current_node = next_node

        self.logger.log("dag_complete", {"message": "Execution finished"})
        return state
