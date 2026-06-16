# Topic: Exception Handling
# Example: Validate file extension

def validate_csv(file_name):
    if not file_name.endswith(".csv"):
        raise ValueError("Only CSV files are allowed")
    print("Valid CSV file")

try:
    validate_csv("employees.xlsx")
except ValueError as error:
    print("Validation error:", error)
