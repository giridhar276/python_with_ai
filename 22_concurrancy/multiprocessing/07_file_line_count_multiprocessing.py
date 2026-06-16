"""
Multiprocessing Example 7: File Line Count

Use Case:
Count lines from multiple files in parallel.
"""

from concurrent.futures import ProcessPoolExecutor
from pathlib import Path


def count_lines(file_path):
    lines = file_path.read_text(encoding="utf-8").splitlines()
    return file_path.name, len(lines)


if __name__ == "__main__":
    data_dir = Path(__file__).resolve().parents[1] / "data"

    files = [
        data_dir / "employees.csv",
        data_dir / "server.log",
        data_dir / "notes.txt",
    ]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(count_lines, files)

    for file_name, line_count in results:
        print(f"{file_name}: {line_count} lines")
