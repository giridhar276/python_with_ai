"""
Multiprocessing Example 9: Log Analysis

Use Case:
Analyze log lines in parallel.
"""

from concurrent.futures import ProcessPoolExecutor
from pathlib import Path


def classify_line(line):
    if "ERROR" in line:
        return "ERROR"
    if "WARNING" in line:
        return "WARNING"
    return "NORMAL"


if __name__ == "__main__":
    log_file = Path(__file__).resolve().parents[1] / "data" / "server.log"
    lines = log_file.read_text(encoding="utf-8").splitlines()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(classify_line, lines))

    print("ERROR count:", results.count("ERROR"))
    print("WARNING count:", results.count("WARNING"))
    print("NORMAL count:", results.count("NORMAL"))
