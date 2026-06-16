"""Writing CSV using the csv module."""

# Read the code from top to bottom and execute it before modifying it.
# Keep the print statements while learning so the flow remains visible.

# This script is designed to run independently from the command line.
# The input data is kept small so learners can understand each step clearly.
# Modify the sample values and rerun the file to observe how the output changes.

import csv
from pathlib import Path

path = Path(__file__).with_name("sample_output.csv")
with path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "score"])
    writer.writerow(["Asha", 90])
print(path.read_text(encoding="utf-8"))
