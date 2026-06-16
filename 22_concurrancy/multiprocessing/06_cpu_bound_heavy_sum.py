"""
Multiprocessing Example 6: CPU-bound Heavy Calculation

Concept:
For CPU-heavy calculations, multiprocessing can use multiple CPU cores.

Threading is not ideal for this because of Python's GIL.
"""

from concurrent.futures import ProcessPoolExecutor


def heavy_sum(limit):
    total = 0

    # This loop simulates CPU-heavy calculation.
    for number in range(limit):
        total += number * number

    return total


if __name__ == "__main__":
    limits = [500000, 600000, 700000, 800000]

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(heavy_sum, limits)

    for result in results:
        print(result)
