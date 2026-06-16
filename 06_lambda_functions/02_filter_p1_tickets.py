# Topic: Lambda Functions
# Example: Filter P1 tickets

tickets = [
    {"id": "INC001", "priority": "P1"},
    {"id": "INC002", "priority": "P3"},
    {"id": "INC003", "priority": "P1"}
]

# filter() keeps only the records that match the lambda condition.
p1_tickets = list(filter(lambda ticket: ticket["priority"] == "P1", tickets))

print(p1_tickets)
