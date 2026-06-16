# Topic: OOP Concepts
# Example: 15 abstract class

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPIPayment(Payment):
    def pay(self, amount):
        print('Paid through UPI:', amount)

UPIPayment().pay(1000)
