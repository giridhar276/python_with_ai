# Topic: Dictionaries
# Example: Department salary summary

employees = [
    {"name": "Asha", "department": "IT", "salary": 85000},
    {"name": "John", "department": "IT", "salary": 95000},
    {"name": "Rahul", "department": "HR", "salary": 62000},
]

salary_summary = {}

for emp in employees:
    dept = emp["department"]
    salary = emp["salary"]

    # get() returns existing department total or 0 for a new department.
    salary_summary[dept] = salary_summary.get(dept, 0) + salary

print(salary_summary)
