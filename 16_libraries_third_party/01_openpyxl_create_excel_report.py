# Topic: Third-party Libraries
# Example: Create Excel report

import os

try:
    from openpyxl import Workbook
except ImportError:
    print("Please install openpyxl: pip install openpyxl")
    raise SystemExit

output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "employee_report.xlsx")
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Workbook() creates a new Excel workbook.
workbook = Workbook()

sheet = workbook.active
sheet.title = "Employees"

# append() adds one row to the Excel sheet.
sheet.append(["Name", "Department", "Salary"])
sheet.append(["Asha", "IT", 85000])
sheet.append(["Rahul", "HR", 62000])

# save() writes the workbook to disk.
workbook.save(output_file)

print(output_file)
