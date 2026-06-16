# Topic: Complex Context Manager
# Example: Audit logger

import os
from datetime import datetime

class AuditLogger:
    def __init__(self, log_path):
        self.log_path = log_path

    def __enter__(self):
        self.file = open(self.log_path, "a", encoding="utf-8")
        self.file.write(f"{datetime.now()} - Operation started\n")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.file.write(f"{datetime.now()} - Error: {exc_value}\n")
        self.file.write(f"{datetime.now()} - Operation ended\n")
        self.file.close()

log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "audit_context.log")
os.makedirs(os.path.dirname(log_file), exist_ok=True)

with AuditLogger(log_file) as log:
    log.write("Payroll report generated successfully\n")
