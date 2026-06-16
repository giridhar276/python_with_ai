# Topic: Config Handling
# Example: Validate required config

import os

required_keys = ["APP_NAME", "ENVIRONMENT"]
missing_keys = []

for key in required_keys:
    if not os.getenv(key):
        missing_keys.append(key)

if missing_keys:
    print("Missing:", missing_keys)
else:
    print("All required config values are available")
