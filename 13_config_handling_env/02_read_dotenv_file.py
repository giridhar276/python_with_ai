# Topic: Config Handling
# Example: Read .env file

import os

try:
    from dotenv import load_dotenv
except ImportError:
    print("Please install python-dotenv: pip install python-dotenv")
    raise SystemExit

env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", ".env.example")

# load_dotenv() loads values from the .env file.
load_dotenv(env_file)

print(os.getenv("APP_NAME"))
print(os.getenv("LOG_LEVEL"))
