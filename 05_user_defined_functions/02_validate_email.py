# Topic: User Defined Functions
# Example: Email validation

def is_valid_email(email):
    # split() separates the username and domain parts.
    return "@" in email and "." in email.split("@")[-1]

emails = ["asha@company.com", "wrong-email", "rahul@test"]

for email in emails:
    print(email, is_valid_email(email))
