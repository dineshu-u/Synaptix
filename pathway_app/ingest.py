import pathway as pw

schema = pw.Schema.from_columns(
    ticket_id=int,
    priority=str,
    created_at=str,
    sla_deadline=str
)

tickets = pw.io.csv.read(
    "data/tickets.csv",
    schema=schema,
    mode="streaming"
)

pw.run()
