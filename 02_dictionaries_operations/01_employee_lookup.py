# Topic: Dictionaries
# Example: Employee lookup

employees = {
    101: {"name": "Asha", "department": "IT", "salary": 85000},
    102: {"name": "Rahul", "department": "HR", "salary": 62000},
    103: {"name": "Meena", "department": "Finance", "salary": 78000}
}

employee_id = 101

# get() avoids KeyError when the key is not available.
employee = employees.get(employee_id)

if employee:
    print("Employee details:", employee)
else:
    print("Employee not found")
