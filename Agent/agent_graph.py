from langgraph.graph import StateGraph
from agents.monitoring_agent import monitoring_agent
from agents.risk_agent import risk_agent
from agents.escalation_agent import escalation_agent

def build_agent_graph():
    graph = StateGraph(dict)

    graph.add_node("monitor", monitoring_agent)
    graph.add_node("risk", risk_agent)
    graph.add_node("escalate", escalation_agent)

    graph.set_entry_point("monitor")
    graph.add_edge("monitor", "risk")
    graph.add_edge("risk", "escalate")

    return graph.compile()
