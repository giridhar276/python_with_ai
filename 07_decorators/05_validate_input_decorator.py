# Topic: Decorators
# Example: Input validation decorator

def validate_positive_amount(func):
    def wrapper(amount):
        if amount <= 0:
            print("Amount must be positive")
            return
        return func(amount)
    return wrapper

@validate_positive_amount
def calculate_tax(amount):
    print("Tax:", amount * 0.18)

calculate_tax(10000)
calculate_tax(-500)
