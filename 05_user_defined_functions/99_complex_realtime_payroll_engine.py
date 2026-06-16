# Topic: Complex Functions
# Example: Payroll engine from CSV

import os
import csv

def calculate_bonus(salary, rating):
    if rating >= 4.5:
        return salary * 0.20
    if rating >= 4.0:
        return salary * 0.12
    return salary * 0.05

def calculate_total_compensation(salary, bonus):
    return salary + bonus

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "employees.csv")

# open() is used to read the employee CSV file.
with open(file_path, "r", encoding="utf-8") as file:
    # DictReader reads every row as a dictionary.
    reader = csv.DictReader(file)

    for row in reader:
        salary = float(row["salary"])
        rating = float(row["rating"])

        bonus = calculate_bonus(salary, rating)
        total = calculate_total_compensation(salary, bonus)

        print(row["name"], "Bonus:", round(bonus, 2), "Total:", round(total, 2))
