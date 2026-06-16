# Topic: OOP Concepts
# Example: 03 instance method

class Employee:
    def __init__(self, name):
        self.name = name

    def show_profile(self):
        print('Employee name:', self.name)

emp = Employee('Meena')
emp.show_profile()
