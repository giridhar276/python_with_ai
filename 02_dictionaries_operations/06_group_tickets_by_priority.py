# Topic: Dictionaries
# Example: Group tickets by priority

tickets = [
    {"id": "INC001", "priority": "P1"},
    {"id": "INC002", "priority": "P3"},
    {"id": "INC003", "priority": "P1"},
    {"id": "INC004", "priority": "P2"},
]

grouped = {}

for ticket in tickets:
    priority = ticket["priority"]

    # setdefault() creates an empty list for a new priority.
    # append() adds ticket id into that priority list.
    grouped.setdefault(priority, []).append(ticket["id"])

print(grouped)
