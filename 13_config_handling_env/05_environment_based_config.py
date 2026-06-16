# Topic: Config Handling
# Example: Environment-based config

import os

environment = os.getenv("ENVIRONMENT", "dev")

if environment == "prod":
    db_url = "prod-db.company.com"
elif environment == "qa":
    db_url = "qa-db.company.com"
else:
    db_url = "localhost"

print(db_url)
