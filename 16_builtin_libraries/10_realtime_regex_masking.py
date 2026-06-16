"""Masking sensitive patterns with the re module."""

# Read the code from top to bottom and execute it before modifying it.
# Keep the print statements while learning so the flow remains visible.

# This script is designed to run independently from the command line.
# The input data is kept small so learners can understand each step clearly.
# Modify the sample values and rerun the file to observe how the output changes.

import re

text = "Contact asha@example.com from 10.20.30.40 for case CS12345"
patterns = [
    (r"[\w.-]+@[\w.-]+", "<EMAIL>"),
    (r"\d{1,3}(?:\.\d{1,3}){3}", "<IP>"),
    (r"CS\d+", "<CASE>"),
]

for pattern, replacement in patterns:
    text = re.sub(pattern, replacement, text)
print(text)
