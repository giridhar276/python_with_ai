# Topic: OOP Concepts
# Example: 05 encapsulation private variable

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

emp = Employee(85000)
print(emp.get_salary())
