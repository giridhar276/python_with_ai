# Topic: Context Manager
# Example: Custom file logger

class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed safely")

with FileLogger("custom_log.txt") as log:
    log.write("Application started")
