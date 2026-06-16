"""Counting events from JSON data."""

# Read the code from top to bottom and execute it before modifying it.
# Keep the print statements while learning so the flow remains visible.

# This script is designed to run independently from the command line.
# The input data is kept small so learners can understand each step clearly.
# Modify the sample values and rerun the file to observe how the output changes.

import json
from pathlib import Path
from collections import Counter

path = Path(__file__).with_name("events.json")
events = json.loads(path.read_text(encoding="utf-8"))
counts = Counter(row["event"] for row in events)
print(counts)
