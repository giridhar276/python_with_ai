# Topic: Complex Lambda Functions
# Example: Employee transform pipeline from CSV

import os
import csv

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "employees.csv")

# open() is used to read the employee CSV file.
with open(file_path, "r", encoding="utf-8") as file:
    # list() converts DictReader rows into a list.
    employees = list(csv.DictReader(file))

# filter() keeps only IT employees.
it_employees = list(filter(lambda emp: emp["department"] == "IT", employees))

# map() creates a new structure with name and salary.
salary_records = list(map(lambda emp: {"name": emp["name"], "salary": float(emp["salary"])}, it_employees))

# sorted() sorts employees by salary.
sorted_records = sorted(salary_records, key=lambda emp: emp["salary"], reverse=True)

for record in sorted_records:
    print(record["name"], record["salary"])
