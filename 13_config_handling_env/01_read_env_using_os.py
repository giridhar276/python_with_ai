# Topic: Config Handling
# Example: Read environment variables

import os

# getenv() reads value from environment variable or returns default.
app_name = os.getenv("APP_NAME", "DefaultApp")
environment = os.getenv("ENVIRONMENT", "local")

print(app_name)
print(environment)
