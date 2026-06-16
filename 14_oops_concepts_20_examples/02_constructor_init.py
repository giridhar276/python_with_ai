# Topic: OOP Concepts
# Example: 02 constructor init

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

emp = Employee('Rahul', 'HR')
print(emp.name, emp.department)
