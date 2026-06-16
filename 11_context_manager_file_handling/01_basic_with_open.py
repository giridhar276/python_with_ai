# Topic: Context Manager
# Example: Basic with open

import os

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "employees.csv")

# with automatically closes the file.
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
