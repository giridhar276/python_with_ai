# Topic: For Loop
# Example: Monthly sales target check

sales_team = {
    "Asha": 125000,
    "Rahul": 85000,
    "Meena": 150000,
    "John": 92000
}

target = 100000

# items() returns key-value pairs from the dictionary.
for name, sales_amount in sales_team.items():
    if sales_amount >= target:
        print(name, "achieved the target")
    else:
        print(name, "did not achieve the target")
