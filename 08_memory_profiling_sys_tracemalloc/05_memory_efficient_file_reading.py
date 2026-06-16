# Topic: Memory Profiling
# Example: Memory efficient file reading

import os

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "employees.csv")

# open() is used to read the file line by line.
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        # strip() removes newline characters.
        print(line.strip())
