# Topic: Large File Handling
# Example: Read large file line by line

import os

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "large_sales.csv")

if not os.path.exists(file_path):
    print("Run 01_generate_large_csv.py first")
else:
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if line_number <= 5:
                print(line.strip())
