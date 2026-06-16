# Topic: OOP Concepts
# Example: 13 static method

class Validator:
    @staticmethod
    def is_valid_email(email):
        return '@' in email

print(Validator.is_valid_email('test@company.com'))
