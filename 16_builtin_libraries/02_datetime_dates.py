"""Working with dates using datetime."""

# Read the code from top to bottom and execute it before modifying it.
# Keep the print statements while learning so the flow remains visible.

# This script is designed to run independently from the command line.
# The input data is kept small so learners can understand each step clearly.
# Modify the sample values and rerun the file to observe how the output changes.

from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))
print((now + timedelta(days=7)).date())
