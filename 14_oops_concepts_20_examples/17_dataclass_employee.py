# Topic: OOP Concepts
# Example: 17 dataclass employee

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    department: str
    salary: float

print(Employee('Asha', 'IT', 85000))
