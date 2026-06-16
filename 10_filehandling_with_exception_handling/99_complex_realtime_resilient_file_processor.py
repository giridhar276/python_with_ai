# Topic: Complex Exception Handling
# Example: Resilient employee CSV processor

import os
import csv
import logging

root = os.path.dirname(os.path.dirname(__file__))
log_file = os.path.join(root, "outputs", "processor_errors.log")
os.makedirs(os.path.dirname(log_file), exist_ok=True)

logging.basicConfig(filename=log_file, level=logging.ERROR)

csv_file = os.path.join(root, "data", "employees.csv")

try:
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                salary = float(row["salary"])

                if salary <= 0:
                    raise ValueError("Salary must be positive")

                print(row["name"], "salary valid")

            except Exception as row_error:
                logging.error("Row processing failed: %s", row_error)

except FileNotFoundError:
    print("Input CSV file not found")
