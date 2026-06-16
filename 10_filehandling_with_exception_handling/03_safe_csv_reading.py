# Topic: Exception Handling
# Example: Safe CSV reading

import os
import csv

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "employees.csv")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"], row["department"])
except FileNotFoundError:
    print("CSV file missing")
except KeyError as error:
    print("Required column missing:", error)
finally:
    print("CSV reading completed")
