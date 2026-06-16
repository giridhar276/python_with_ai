"""
Multiprocessing Example 1: Basic Process

Concept:
A process has its own Python interpreter and memory.
Multiprocessing is useful for CPU-bound tasks.

Important:
Always use if __name__ == "__main__" for multiprocessing,
especially on Windows and macOS.
"""

import multiprocessing
import os


def task():
    print("Task running inside process ID:", os.getpid())


if __name__ == "__main__":
    process = multiprocessing.Process(target=task)
    process.start()
    process.join()

    print("Main process completed")
