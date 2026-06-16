"""
Example 1: Generate Secure Tokens

Use Case:
- API tokens
- Session tokens
- Password reset tokens
- Email verification tokens
"""

import secrets

token_hex = secrets.token_hex(16)
token_urlsafe = secrets.token_urlsafe(32)

print("Hex Token:", token_hex)
print("URL Safe Token:", token_urlsafe)

print("\nExplanation:")
print("token_hex is useful for general secret tokens.")
print("token_urlsafe is useful for URLs, reset links, and verification links.")
