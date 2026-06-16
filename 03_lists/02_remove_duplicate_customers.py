# Topic: Lists
# Example: Remove duplicate customers

customers = ["IBM", "TCS", "IBM", "Wipro", "TCS", "Infosys"]
unique_customers = []

for customer in customers:
    if customer not in unique_customers:
        # append() adds the customer only when it is not already present.
        unique_customers.append(customer)

print(unique_customers)
