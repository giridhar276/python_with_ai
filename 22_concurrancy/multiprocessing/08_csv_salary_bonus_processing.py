"""
Multiprocessing Example 8: CSV Salary Bonus Processing

Use Case:
Process employee rows independently.
This pattern can be used for large CSV transformations.
"""

from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
import csv


def calculate_bonus(row):
    salary = float(row["salary"])
    bonus = salary * 0.10
    return row["name"], salary, bonus


if __name__ == "__main__":
    csv_file = Path(__file__).resolve().parents[1] / "data" / "employees.csv"

    with csv_file.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    with ProcessPoolExecutor(max_workers=2) as executor:
        results = executor.map(calculate_bonus, rows)

    for name, salary, bonus in results:
        print(f"{name}: Salary={salary}, Bonus={bonus}")
