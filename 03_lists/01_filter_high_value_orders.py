# Topic: Lists
# Example: Filter high-value orders

orders = [12000, 45000, 7000, 88000, 23000]
high_value_orders = []

for amount in orders:
    if amount >= 25000:
        # append() adds a matching amount into the result list.
        high_value_orders.append(amount)

print(high_value_orders)
