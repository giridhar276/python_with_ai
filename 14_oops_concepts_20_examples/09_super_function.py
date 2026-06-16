# Topic: OOP Concepts
# Example: 09 super function

class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

mgr = Manager('Asha', 8)
print(mgr.name, mgr.team_size)
