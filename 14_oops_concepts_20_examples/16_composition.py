# Topic: OOP Concepts
# Example: 16 composition

class Address:
    def __init__(self, city):
        self.city = city

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

emp = Employee('Asha', Address('Bangalore'))
print(emp.name, emp.address.city)
