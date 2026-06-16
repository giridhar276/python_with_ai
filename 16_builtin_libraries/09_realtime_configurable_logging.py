"""Creating a configurable logger."""

# Read the code from top to bottom and execute it before modifying it.
# Keep the print statements while learning so the flow remains visible.

# This script is designed to run independently from the command line.
# The input data is kept small so learners can understand each step clearly.
# Modify the sample values and rerun the file to observe how the output changes.

import logging
from pathlib import Path

log_path = Path(__file__).with_name("app.log")
logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("application started")
logging.error("sample error for training")
print(log_path.read_text(encoding="utf-8"))
