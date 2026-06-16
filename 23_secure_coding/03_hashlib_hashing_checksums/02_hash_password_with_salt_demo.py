"""
Example 2: Hash Password with Salt - Demonstration

Important:
For real password storage, prefer:
- bcrypt
- argon2
- passlib
- werkzeug.security

This example demonstrates the idea of salt using hashlib.

Salt:
A random value added to password before hashing.
It prevents same passwords from producing same hash.
"""

import hashlib
import secrets

def hash_password(password):
    salt = secrets.token_hex(16)
    combined = salt + password

    password_hash = hashlib.sha256(combined.encode("utf-8")).hexdigest()

    return salt, password_hash


def verify_password(password, salt, stored_hash):
    combined = salt + password
    new_hash = hashlib.sha256(combined.encode("utf-8")).hexdigest()

    return new_hash == stored_hash


user_password = "MySecurePassword@123"

salt, stored_hash = hash_password(user_password)

print("Salt:", salt)
print("Stored Password Hash:", stored_hash)

login_password = "MySecurePassword@123"

if verify_password(login_password, salt, stored_hash):
    print("Password verification successful.")
else:
    print("Invalid password.")
