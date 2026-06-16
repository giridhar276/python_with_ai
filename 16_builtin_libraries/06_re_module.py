"""Extracting values with regular expressions."""

# Read the code from top to bottom and execute it before modifying it.
# Keep the print statements while learning so the flow remains visible.

# This script is designed to run independently from the command line.
# The input data is kept small so learners can understand each step clearly.
# Modify the sample values and rerun the file to observe how the output changes.

import re

text = "Case CS12345 failed at 10:30 with status 500"
match = re.search(r"CS\d+", text)
print(match.group() if match else "not found")
