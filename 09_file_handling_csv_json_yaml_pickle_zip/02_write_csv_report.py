# Topic: File Handling
# Example: Write CSV

import os
import csv

output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "sales_summary.csv")

# makedirs() creates the output folder if it does not exist.
os.makedirs(os.path.dirname(output_file), exist_ok=True)

rows = [
    {"region": "South", "total_sales": 250000},
    {"region": "North", "total_sales": 140000}
]

# open() is used to write the CSV file.
with open(output_file, "w", newline="", encoding="utf-8") as file:
    # DictWriter writes dictionaries into CSV format.
    writer = csv.DictWriter(file, fieldnames=["region", "total_sales"])

    writer.writeheader()
    writer.writerows(rows)

print(output_file)
