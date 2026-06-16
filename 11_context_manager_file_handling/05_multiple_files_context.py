# Topic: Context Manager
# Example: Copy file using multiple context managers

import os

root = os.path.dirname(os.path.dirname(__file__))
input_file = os.path.join(root, "data", "employees.csv")
output_file = os.path.join(root, "outputs", "employees_copy.csv")

os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(input_file, "r", encoding="utf-8") as src, open(output_file, "w", encoding="utf-8") as dest:
    for line in src:
        dest.write(line)

print(output_file)
