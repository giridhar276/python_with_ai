# Topic: Lambda Functions
# Example: Sort employees by salary

employees = [
    {"name": "Asha", "salary": 85000},
    {"name": "Rahul", "salary": 62000},
    {"name": "John", "salary": 95000}
]

# lambda is used as a short function to pick salary for sorting.
sorted_employees = sorted(employees, key=lambda emp: emp["salary"], reverse=True)

print(sorted_employees)
