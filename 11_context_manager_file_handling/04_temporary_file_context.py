# Topic: Context Manager
# Example: Temporary file

import tempfile

# NamedTemporaryFile creates a temporary file and removes it automatically.
with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
    temp_file.write("Temporary training data")
    temp_file.seek(0)
    print(temp_file.read())

print("Temporary file removed")
