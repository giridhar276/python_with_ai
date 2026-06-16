"""Managing paths with pathlib."""

# Read the code from top to bottom and execute it before modifying it.
# Keep the print statements while learning so the flow remains visible.

# This script is designed to run independently from the command line.
# The input data is kept small so learners can understand each step clearly.
# Modify the sample values and rerun the file to observe how the output changes.

from pathlib import Path

path = Path(__file__)
print(path.name)
print(path.parent)
print(path.suffix)
