# Topic: Nested Loop
# Example: Department-wise employee report

departments = {
    "IT": ["Asha", "John", "Kiran"],
    "HR": ["Rahul"],
    "Finance": ["Meena", "Priya"]
}

# items() returns each department and its employee list.
for department, employees in departments.items():
    print("\nDepartment:", department)

    for employee in employees:
        print(" -", employee)
