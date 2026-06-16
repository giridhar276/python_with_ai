# Topic: Large File Handling
# Example: Generate large CSV

import os
import csv

output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "large_sales.csv")
os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["order_id", "amount"])

    for i in range(1, 10001):
        writer.writerow([f"O{i}", i * 10])

print(output_file)
