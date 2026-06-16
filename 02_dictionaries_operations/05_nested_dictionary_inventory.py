# Topic: Nested Dictionaries
# Example: Inventory update

inventory = {
    "Laptop": {"stock": 10, "price": 65000},
    "Mouse": {"stock": 100, "price": 700}
}

inventory["Laptop"]["stock"] -= 2
inventory["Keyboard"] = {"stock": 50, "price": 1200}

print(inventory)
