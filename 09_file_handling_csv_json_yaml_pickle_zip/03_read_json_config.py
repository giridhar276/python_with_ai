# Topic: File Handling
# Example: Read JSON

import os
import json

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "app_config.json")

with open(file_path, "r", encoding="utf-8") as file:
    # json.load() converts JSON file content into Python data.
    config = json.load(file)

print(config["app_name"])
print(config["environment"])
