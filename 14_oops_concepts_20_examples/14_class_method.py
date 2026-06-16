# Topic: OOP Concepts
# Example: 14 class method

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    @classmethod
    def from_csv_row(cls, row):
        name, department = row.split(',')
        return cls(name, department)

emp = Employee.from_csv_row('Asha,IT')
print(emp.name, emp.department)
