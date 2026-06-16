# Topic: User Defined Functions
# Example: Variable arguments

def total_expense(*amounts):
    # sum() adds all values from the tuple.
    return sum(amounts)

print(total_expense(1200, 450, 900, 300))
