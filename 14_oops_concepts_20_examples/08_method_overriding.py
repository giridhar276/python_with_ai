# Topic: OOP Concepts
# Example: 08 method overriding

class Employee:
    def bonus(self):
        return 5000

class Manager(Employee):
    def bonus(self):
        return 10000

print(Employee().bonus())
print(Manager().bonus())
