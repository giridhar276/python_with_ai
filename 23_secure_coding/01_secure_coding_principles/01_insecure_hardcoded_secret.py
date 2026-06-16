"""
Example 1: Insecure Hardcoded Secret

Concept:
Hardcoding passwords, API keys, and tokens directly in source code is unsafe.

Why unsafe?
- Code may be pushed to GitHub.
- Other team members may see it.
- Logs or screenshots may expose it.
- Changing the secret requires code change.

This example is intentionally insecure.
"""

# BAD PRACTICE: Never do this in real projects.
API_KEY = "my-production-api-key-12345"
DB_PASSWORD = "Admin@123"

print("Connecting to service using hardcoded API key...")
print("This is insecure because secrets are visible in code.")

# Notice:
# We are not printing the actual secret.
# Even printing secrets is also a bad practice.
