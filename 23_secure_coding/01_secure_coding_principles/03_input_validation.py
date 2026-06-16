"""
Example 3: Input Validation

Concept:
Never trust user input directly.

This example validates age input.
"""

def register_user(name, age_text):
    # Validate name
    if not name or not name.strip():
        raise ValueError("Name cannot be empty.")

    # Validate age
    if not age_text.isdigit():
        raise ValueError("Age must be a number.")

    age = int(age_text)

    if age < 18 or age > 100:
        raise ValueError("Age must be between 18 and 100.")

    return {
        "name": name.strip(),
        "age": age,
        "status": "registered"
    }


try:
    user_name = input("Enter name: ")
    user_age = input("Enter age: ")

    result = register_user(user_name, user_age)
    print("User registered successfully:", result)

except ValueError as error:
    print("Validation Error:", error)
