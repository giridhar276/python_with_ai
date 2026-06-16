# Topic: Conditions with Loop
# Example: Inventory reorder alert

inventory = [
    {"item": "Laptop", "stock": 5, "reorder_level": 10},
    {"item": "Mouse", "stock": 100, "reorder_level": 30},
    {"item": "Keyboard", "stock": 8, "reorder_level": 20},
]

for product in inventory:
    if product["stock"] <= product["reorder_level"]:
        print("Reorder needed for:", product["item"])
    else:
        print("Stock is sufficient for:", product["item"])
