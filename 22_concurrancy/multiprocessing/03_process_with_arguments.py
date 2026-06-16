"""
Multiprocessing Example 3: Passing Arguments to a Process

Concept:
args is used to send values to the function executed by a process.
"""

import multiprocessing


def calculate_square(number):
    print(f"Square of {number} is {number * number}")


if __name__ == "__main__":
    process = multiprocessing.Process(target=calculate_square, args=(10,))
    process.start()
    process.join()
