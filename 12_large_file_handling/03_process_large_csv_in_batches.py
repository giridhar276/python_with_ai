# Topic: Large File Handling
# Example: Process CSV in batches

import os
import csv

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "large_sales.csv")
batch = []
batch_size = 1000

if not os.path.exists(file_path):
    print("Run 01_generate_large_csv.py first")
else:
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            batch.append(row)

            if len(batch) == batch_size:
                print("Processing batch of", len(batch), "records")
                batch.clear()

        if batch:
            print("Processing final batch of", len(batch), "records")
