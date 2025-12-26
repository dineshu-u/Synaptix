def escalation_agent(state):
    if state.get("decision") == "ESCALATE":
        print(
            f"⚠️ SLA BREACH LIKELY | Ticket {state['ticket_id']} | Priority {state['priority']}"
        )
    return state
