# Topic: Exception Handling
# Example: Log errors to file

import os
import logging

log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "error.log")
os.makedirs(os.path.dirname(log_file), exist_ok=True)

# basicConfig() configures logging output file and level.
logging.basicConfig(filename=log_file, level=logging.ERROR)

try:
    result = 10 / 0
except ZeroDivisionError as error:
    # logging.error() writes error details to log file.
    logging.error("Error occurred: %s", error)
    print("Error logged to:", log_file)
