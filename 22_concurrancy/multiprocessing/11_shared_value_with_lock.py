"""
Multiprocessing Example 11: Shared Value with Lock

Concept:
multiprocessing.Value creates shared memory for a simple value.
get_lock() protects the value from race conditions.
"""

import multiprocessing


def increment(counter):
    for _ in range(1000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = multiprocessing.Value("i", 0)

    processes = []

    for _ in range(5):
        process = multiprocessing.Process(target=increment, args=(counter,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Final counter:", counter.value)
