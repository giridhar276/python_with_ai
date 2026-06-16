# Topic: Exception Handling
# Example: Safe write with backup

import os
import shutil

output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "report.txt")
os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, "w", encoding="utf-8") as file:
    file.write("Old report")

try:
    backup_file = output_file + ".bak"

    # shutil.copy() creates a backup before overwrite.
    shutil.copy(output_file, backup_file)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("New report")

    print("Backup created:", backup_file)
except Exception as error:
    print("Failed to update file:", error)
