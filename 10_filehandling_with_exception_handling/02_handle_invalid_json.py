# Topic: Exception Handling
# Example: Handle invalid JSON

import os
import json

output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "invalid.json")
os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, "w", encoding="utf-8") as file:
    file.write("{invalid json}")

try:
    with open(output_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        print(data)
except json.JSONDecodeError as error:
    print("Invalid JSON format:", error)
