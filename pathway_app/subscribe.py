import pathway as pw
from pathway_app.sla_risk import add_risk
from agents.agent_graph import build_agent_graph
from pathway_app.ingest import tickets

agent_flow = build_agent_graph()

tickets_with_risk = add_risk(tickets)

high_risk = tickets_with_risk.filter(pw.this.risk == "HIGH")

def run_agents(row):
    agent_flow.invoke({
        "ticket_id": row.ticket_id,
        "priority": row.priority,
        "risk": row.risk
    })

pw.io.subscribe(high_risk, run_agents)
pw.run()
