import time
import random
import csv
from datetime import datetime, timedelta

def generate_ticket():
    priority = random.choice(["P1", "P2", "P3"])
    sla_minutes = {"P1": 30, "P2": 60, "P3": 120}[priority]

    return {
        "ticket_id": random.randint(1000, 9999),
        "priority": priority,
        "created_at": datetime.now().isoformat(),
        "sla_deadline": (datetime.now() + timedelta(minutes=sla_minutes)).isoformat()
    }

with open("data/tickets.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["ticket_id", "priority", "created_at", "sla_deadline"]
    )
    writer.writeheader()

    print("🚀 Ticket stream started...")
    while True:
        ticket = generate_ticket()
        writer.writerow(ticket)
        f.flush()
        print("New ticket:", ticket)
        time.sleep(random.randint(2, 5))
