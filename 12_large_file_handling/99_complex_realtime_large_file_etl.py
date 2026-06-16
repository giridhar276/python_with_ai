# Topic: Complex Large File Handling
# Example: Large file ETL

import os
import csv

root = os.path.dirname(os.path.dirname(__file__))
large_file = os.path.join(root, "outputs", "etl_large_sales.csv")
os.makedirs(os.path.dirname(large_file), exist_ok=True)

with open(large_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["order_id", "amount"])

    for i in range(1, 50001):
        writer.writerow([f"O{i}", i * 5])

batch_size = 10000
batch_total = 0
batch_count = 0
grand_total = 0

with open(large_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        batch_total += float(row["amount"])
        batch_count += 1

        if batch_count == batch_size:
            print("Processed batch total:", batch_total)
            grand_total += batch_total
            batch_total = 0
            batch_count = 0

if batch_count > 0:
    grand_total += batch_total

print("Grand total:", grand_total)
