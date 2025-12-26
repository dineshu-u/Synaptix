def risk_agent(state):
    if state["risk"] == "HIGH":
        state["decision"] = "ESCALATE"
    return state
