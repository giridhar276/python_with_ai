# Topic: Conditions with Calculation
# Example: Employee attendance status

working_days = 22

employees = {
    "Asha": 21,
    "Rahul": 16,
    "Meena": 19,
    "John": 22
}

# items() returns employee name and present days.
for name, present_days in employees.items():
    attendance_percentage = present_days / working_days * 100

    if attendance_percentage >= 90:
        status = "Excellent"
    elif attendance_percentage >= 75:
        status = "Good"
    else:
        status = "Needs improvement"

    # round() limits the percentage to two decimal places.
    print(name, "Attendance:", round(attendance_percentage, 2), "%", "-", status)
