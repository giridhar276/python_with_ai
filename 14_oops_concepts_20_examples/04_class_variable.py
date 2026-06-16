# Topic: OOP Concepts
# Example: 04 class variable

class Employee:
    company = 'ABC Technologies'

    def __init__(self, name):
        self.name = name

emp1 = Employee('Asha')
emp2 = Employee('John')
print(emp1.name, emp1.company)
print(emp2.name, emp2.company)
