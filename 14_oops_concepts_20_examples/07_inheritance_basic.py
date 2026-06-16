# Topic: OOP Concepts
# Example: 07 inheritance basic

class Employee:
    def work(self):
        print('Employee is working')

class Manager(Employee):
    def conduct_meeting(self):
        print('Manager is conducting meeting')

mgr = Manager()
mgr.work()
mgr.conduct_meeting()
