"""
Multiprocessing Example 2: Multiple Processes

Concept:
Create multiple independent processes.

Use Case:
Run multiple CPU-heavy jobs in parallel.
"""

import multiprocessing
import os


def work(task_id):
    print(f"Task {task_id} is running in process ID {os.getpid()}")


if __name__ == "__main__":
    processes = []

    for task_id in range(1, 6):
        process = multiprocessing.Process(target=work, args=(task_id,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes completed")
