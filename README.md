Multi-Agent Debate DAG (LangGraph-Compatible)
ATG Technical Assignment — Machine Learning Intern
Objective
Design and implement a multi-agent debate system using a directed acyclic graph (DAG) architecture inspired by LangGraph, where two AI agents engage in a structured debate under strict rules.
The system:
•	Runs exactly 8 rounds (4 turns per agent, alternating)
•	Preserves and updates structured debate memory
•	Supplies each agent with only relevant memory for its next turn
•	Enforces turn order, round limits, and no repetition
•	Concludes with a JudgeNode that summarizes the debate and declares a winner
•	Operates entirely via a clean CLI
•	Logs every node execution and state transition to a persistent log file
System Architecture Overview
The system is implemented as a LangGraph-compatible DAG execution engine, where:
•	Each node is a pure function
•	A single global state (DebateState) flows through the graph
•	Routing decisions are made explicitly by a controller node
•	Execution terminates at a dedicated Judge node
DAG Diagram

diretly in github repo

DAG Flow Description
UserInputNode
     ↓
ControllerNode
     ↓
AgentA / AgentB (alternating)
     ↓
MemoryNode
     ↓
ControllerNode
     ↓
(After 8 rounds)
JudgeNode
     ↓
END
Node Responsibilities
UserInputNode
•	Accepts debate topic via CLI
•	Validates and sanitizes input
•	Initializes debate state
ControllerNode
•	Enforces exactly 8 rounds
•	Guarantees strict alternation
•	Routes execution to the correct agent or Judge
AgentA (Scientist) / AgentB (Philosopher)
•	Generate one argument per turn
•	Receive only relevant memory slices
•	Do not control routing or state persistence
MemoryNode
•	Commits arguments to debate history
•	Updates repetition tracking
•	Logs each completed turn
•	Routes back to Controller
JudgeNode
•	Aggregates full debate history
•	Produces:
o	Debate summary
o	Winner declaration
o	Reasoned justification
•	Terminates the DAG
Memory Structure
{
  "turns": [
    {"round": 1, "agent": "AgentA", "text": "..."},
    {"round": 2, "agent": "AgentB", "text": "..."}
  ],
  "used_arguments": {
    "AgentA": [...],
    "AgentB": [...]
  }
}
Each agent receives only:
•	Debate topic
•	Opponent’s last argument
•	Its own prior arguments
CLI Usage
Run the debate:
python run_debate.py
Example interaction:
Enter topic for debate: Should AI be regulated like medicine?

[Round 1] AgentA: ...
[Round 2] AgentB: ...
...
[Round 8] AgentB: ...

=== JUDGE SUMMARY ===
Winner: AgentB
Reason: Demonstrated stronger philosophical reasoning and abstraction.

Logging
•	All node executions and state transitions are logged
•	Format: JSON Lines
•	Location:
logs/debate_log.json
This includes:
•	Node entry/exit
•	Turn commits
•	Routing decisions
•	Final verdict
LangGraph Compatibility Note
Due to a 32-bit Windows environment, the official langgraph Python package (which requires 64-bit Python) could not be installed.
To address this, the project implements a LangGraph-compatible DAG execution engine with:
•	Explicit node definitions
•	State passing semantics
•	Router-based control flow
•	Terminal node termination
•	Visual DAG representation
The design, semantics, and execution model mirror LangGraph principles exactly, while remaining platform-compatible.
Project Structure
debate/
├── run_debate.py
├── dag_executor.py
├── generate_dag.py
├── dag.png
├── nodes/
│   ├── user_input_node.py
│   ├── controller_node.py
│   ├── agent_node.py
│   ├── agent_logic.py
│   ├── memory_node.py
│   ├── memory_utils.py
│   ├── judge_node.py
│   └── logger_node.py
├── state/
│   └── debate_state.py
├── personas/
│   ├── scientist.txt
│   └── philosopher.txt
├── logs/
│   └── debate_log.json
└── README.md

Deliverables Checklist
 Multi-agent debate system
 DAG-based execution
 Strict turn control (8 rounds)
 Memory slicing
 JudgeNode with justification
 CLI interface
 Persistent logs
 DAG diagram (Graphviz)
Demo
A short demo video shows:
•	CLI execution
•	Sample debate rounds
•	Judge summary
•	Log file inspection
Conclusion
This project demonstrates:
•	Multi-agent orchestration
•	DAG-based workflow design
•	Controlled state management
•	Audit-friendly logging
•	Practical handling of platform constraints
It reflects real-world AI agent system engineering pr

