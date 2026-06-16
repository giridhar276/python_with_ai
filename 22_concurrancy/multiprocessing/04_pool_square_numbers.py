"""
Multiprocessing Example 4: Pool

Concept:
Pool manages a group of worker processes.

Use Case:
Apply the same function to many input values.
"""

from multiprocessing import Pool


def square(number):
    return number * number


if __name__ == "__main__":
    numbers = list(range(1, 11))

    # processes=4 means 4 worker processes.
    with Pool(processes=4) as pool:
        results = pool.map(square, numbers)

    print(results)
