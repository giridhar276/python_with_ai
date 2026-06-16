"""
Threading Example 9: Log Error Search

Real-time Use Case:
Search ERROR and WARNING lines from application logs.

This pattern is useful in monitoring and log analyzer tools.
"""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


log_file = Path(__file__).resolve().parents[1] / "data" / "server.log"
lines = log_file.read_text(encoding="utf-8").splitlines()


def classify_log_line(line):
    # Check if the line contains ERROR.
    if "ERROR" in line:
        return "ERROR", line

    # Check if the line contains WARNING.
    if "WARNING" in line:
        return "WARNING", line

    # Otherwise treat it as normal log.
    return "NORMAL", line


with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(classify_log_line, lines)

for level, line in results:
    if level != "NORMAL":
        print(level, "->", line)
