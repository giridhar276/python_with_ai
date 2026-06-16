# Topic: Nested Conditions
# Example: Ticket priority escalation

priority = "P1"
hours_open = 6
status = "Open"

if status == "Open":
    if priority == "P1" and hours_open > 2:
        print("Escalate to crisis management team")
    elif priority == "P2" and hours_open > 8:
        print("Escalate to L2 support team")
    else:
        print("Continue monitoring")
else:
    print("Ticket already closed")
