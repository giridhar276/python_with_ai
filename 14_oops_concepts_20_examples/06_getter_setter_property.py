# Topic: OOP Concepts
# Example: 06 getter setter property

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value

emp = Employee(50000)
emp.salary = 60000
print(emp.salary)
