# Topic: File Handling
# Example: Read CSV

import os
import csv

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "sales.csv")

# open() is used to read the CSV file.
with open(file_path, "r", encoding="utf-8") as file:
    # DictReader reads rows as dictionaries.
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
