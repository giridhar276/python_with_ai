"""
Threading Example 8: Reading Multiple Files Concurrently

Real-time Use Case:
Read multiple configuration, CSV, log, or text files.

Why threading?
File reading is I/O-bound, so threads can help when reading many files.
"""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


# Get path to the data folder.
data_dir = Path(__file__).resolve().parents[1] / "data"

files = [
    data_dir / "employees.csv",
    data_dir / "server.log",
    data_dir / "notes.txt",
]


def read_file(file_path):
    # Read file content.
    content = file_path.read_text(encoding="utf-8")

    # Return file name and size.
    return file_path.name, len(content)


with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(read_file, files)

for file_name, size in results:
    print(f"{file_name}: {size} characters")
