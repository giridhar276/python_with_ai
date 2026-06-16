# Topic: OOP Concepts
# Example: 18 custom exception class

class InvalidSalaryError(Exception):
    pass

def update_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError('Salary must be positive')
    print('Salary updated:', salary)

try:
    update_salary(-1000)
except InvalidSalaryError as error:
    print(error)
