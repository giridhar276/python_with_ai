# Topic: Complex Lists
# Example: Sales processing pipeline from CSV

import os
import csv

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "sales.csv")
processed_orders = []

# open() is used to read the sales CSV file.
with open(file_path, "r", encoding="utf-8") as file:
    # DictReader reads every row as a dictionary.
    reader = csv.DictReader(file)

    for row in reader:
        quantity = int(row["quantity"])
        price = float(row["price"])
        total_amount = quantity * price
        row["total_amount"] = total_amount

        if row["status"] == "Delivered":
            # append() adds delivered order into the result list.
            processed_orders.append(row)

# sort() rearranges the existing list in-place.
processed_orders.sort(key=lambda order: order["total_amount"], reverse=True)

for order in processed_orders:
    print(order["order_id"], order["customer"], order["total_amount"])
