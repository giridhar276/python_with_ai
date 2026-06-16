"""
Example 4: Compare File Checksum

Use Case:
Verify whether a file has changed.

Step:
1. Create file
2. Calculate checksum
3. Modify file
4. Calculate checksum again
5. Compare both checksums
"""

import hashlib
from pathlib import Path

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()


file_path = Path("important_file.txt")

file_path.write_text("Original file content", encoding="utf-8")
original_checksum = calculate_sha256(file_path)

file_path.write_text("Modified file content", encoding="utf-8")
modified_checksum = calculate_sha256(file_path)

print("Original Checksum:", original_checksum)
print("Modified Checksum:", modified_checksum)

if original_checksum == modified_checksum:
    print("File is unchanged.")
else:
    print("File was modified.")
