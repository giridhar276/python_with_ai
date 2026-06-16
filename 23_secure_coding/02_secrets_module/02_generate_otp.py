"""
Example 2: Generate Secure Numeric OTP

Use Case:
- Login OTP
- Email verification OTP
- Phone verification OTP

Note:
For real production OTP systems, also add:
- Expiry time
- Retry limit
- Rate limiting
- Secure storage
"""

import secrets

def generate_otp(length=6):
    digits = "0123456789"
    otp = "".join(secrets.choice(digits) for _ in range(length))
    return otp


otp = generate_otp()
print("Generated OTP:", otp)
