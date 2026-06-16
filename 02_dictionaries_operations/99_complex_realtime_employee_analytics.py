# Topic: Complex Dictionary Operations
# Example: Employee analytics from CSV

import os
import csv

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "employees.csv")
department_summary = {}

# open() is used to read the CSV file.
with open(file_path, "r", encoding="utf-8") as file:
    # DictReader reads each CSV row as a dictionary.
    reader = csv.DictReader(file)

    for row in reader:
        department = row["department"]

        # float() converts CSV string values into decimal numbers.
        salary = float(row["salary"])
        rating = float(row["rating"])

        # setdefault() creates the default summary structure for a new department.
        department_summary.setdefault(
            department,
            {"count": 0, "total_salary": 0, "total_rating": 0}
        )

        department_summary[department]["count"] += 1
        department_summary[department]["total_salary"] += salary
        department_summary[department]["total_rating"] += rating

# items() returns department name and summary dictionary.
for department, summary in department_summary.items():
    avg_salary = summary["total_salary"] / summary["count"]
    avg_rating = summary["total_rating"] / summary["count"]

    # round() formats average values.
    print(department, "Employees:", summary["count"], "Avg Salary:", round(avg_salary, 2), "Avg Rating:", round(avg_rating, 2))
