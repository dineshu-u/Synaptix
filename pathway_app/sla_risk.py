from datetime import datetime
import pathway as pw

def compute_risk(row):
    deadline = datetime.fromisoformat(row.sla_deadline)
    minutes_left = (deadline - datetime.now()).total_seconds() / 60

    if row.priority == "P1" and minutes_left < 20:
        return "HIGH"
    elif row.priority == "P2" and minutes_left < 30:
        return "MEDIUM"
    else:
        return "LOW"

def add_risk(tickets):
    return tickets.with_columns(
        risk=pw.apply(compute_risk, pw.this)
    )
