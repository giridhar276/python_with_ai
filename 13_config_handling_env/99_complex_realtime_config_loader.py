# Topic: Complex Config Handling
# Example: Config loader from .env and JSON

import os
import json

try:
    from dotenv import load_dotenv
except ImportError:
    print("Please install python-dotenv: pip install python-dotenv")
    raise SystemExit

root = os.path.dirname(os.path.dirname(__file__))
env_file = os.path.join(root, "data", ".env.example")
config_file = os.path.join(root, "data", "app_config.json")

load_dotenv(env_file)

with open(config_file, "r", encoding="utf-8") as file:
    config = json.load(file)

config["app_name"] = os.getenv("APP_NAME", config["app_name"])
config["environment"] = os.getenv("ENVIRONMENT", config["environment"])
config["log_level"] = os.getenv("LOG_LEVEL", config["log_level"])
config["retry_count"] = int(os.getenv("MAX_RETRIES", config["retry_count"]))

print(config)
