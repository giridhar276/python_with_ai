"""
Example 3: Generate File Checksum

Use Case:
- Verify downloaded file integrity
- Check if file was modified
- Detect duplicate files

This script creates a sample file and calculates SHA256 checksum.
"""

import hashlib
from pathlib import Path

sample_file = Path("sample_data.txt")
sample_file.write_text("This is a sample file for checksum demo.", encoding="utf-8")

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()


checksum = calculate_sha256(sample_file)

print("File Name:", sample_file)
print("SHA256 Checksum:", checksum)
