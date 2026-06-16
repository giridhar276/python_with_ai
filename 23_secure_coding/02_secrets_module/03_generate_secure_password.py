"""
Example 3: Generate Secure Random Password

Use Case:
- Temporary password
- Admin-created user password
- Secure test password generation
"""

import secrets
import string

def generate_password(length=14):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


secure_password = generate_password()
print("Generated Secure Password:", secure_password)
