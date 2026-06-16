"""
Example 4: Generate Password Reset Link

Use Case:
When a user clicks "Forgot Password", generate a secure token and send it as a reset link.

Important:
In real applications:
- Store only hashed token in database
- Set expiry time
- Use HTTPS
- Invalidate token after use
"""

import secrets

base_url = "https://example.com/reset-password"
reset_token = secrets.token_urlsafe(32)

reset_link = f"{base_url}?token={reset_token}"

print("Password Reset Link:")
print(reset_link)
