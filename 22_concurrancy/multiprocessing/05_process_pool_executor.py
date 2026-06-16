"""
Multiprocessing Example 5: ProcessPoolExecutor

Concept:
ProcessPoolExecutor is a modern high-level API for multiprocessing.
"""

from concurrent.futures import ProcessPoolExecutor


def cube(number):
    return number ** 3


if __name__ == "__main__":
    numbers = range(1, 8)

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(cube, numbers)

    for result in results:
        print(result)
