"""
Example 4: Safe Error Handling

Concept:
Do not expose internal technical details to users.

Bad:
Printing database connection string, password, full stack trace, internal path.

Good:
Show simple user-friendly error and log internal details securely.
"""

def divide_numbers(a, b):
    return a / b


try:
    result = divide_numbers(10, 0)
    print("Result:", result)

except ZeroDivisionError:
    # User-friendly message
    print("Something went wrong while processing your request.")

    # In real projects:
    # log the technical details into a secure logging system
    # do not expose sensitive internals to end users
