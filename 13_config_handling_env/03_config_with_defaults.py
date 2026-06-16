# Topic: Config Handling
# Example: Config defaults

import os

max_retries = int(os.getenv("MAX_RETRIES", "3"))
timeout = int(os.getenv("TIMEOUT", "30"))

print(max_retries)
print(timeout)
