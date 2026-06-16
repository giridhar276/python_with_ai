# Topic: Complex Conditions
# Example: SLA breach detection from support ticket CSV

import os
import csv

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "support_tickets.csv")

sla_limits = {
    "P1": 4,
    "P2": 12,
    "P3": 24,
    "P4": 48
}

# open() is used to read the CSV file.
with open(file_path, "r", encoding="utf-8") as file:
    # DictReader reads every CSV row as a dictionary.
    reader = csv.DictReader(file)

    for ticket in reader:
        priority = ticket["priority"]
        status = ticket["status"]

        # int() converts CSV string value into integer.
        hours_open = int(ticket["hours_open"])

        # get() safely reads SLA limit and gives default value if priority is missing.
        allowed_hours = sla_limits.get(priority, 24)

        if status == "Open":
            if hours_open > allowed_hours:
                print(ticket["ticket_id"], "SLA BREACHED - escalate")
            elif hours_open >= allowed_hours * 0.8:
                print(ticket["ticket_id"], "Near SLA breach - monitor closely")
            else:
                print(ticket["ticket_id"], "Within SLA")
        else:
            print(ticket["ticket_id"], "Closed ticket - no action required")
