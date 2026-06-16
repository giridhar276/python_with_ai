# Topic: Lists
# Example: Batch processing using slicing

customer_ids = list(range(1001, 1021))
batch_size = 5

# range() moves in steps of batch_size.
for start in range(0, len(customer_ids), batch_size):
    batch = customer_ids[start:start + batch_size]
    print("Processing batch:", batch)
