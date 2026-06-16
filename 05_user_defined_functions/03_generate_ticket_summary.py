# Topic: User Defined Functions
# Example: Ticket summary

def generate_summary(ticket):
    return f"{ticket['id']} | {ticket['priority']} | {ticket['status']}"

ticket = {"id": "INC001", "priority": "P1", "status": "Open"}

print(generate_summary(ticket))
