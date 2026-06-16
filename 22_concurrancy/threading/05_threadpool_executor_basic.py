"""
Threading Example 5: ThreadPoolExecutor

Concept:
ThreadPoolExecutor provides a cleaner way to manage multiple threads.

Advantage:
You do not need to manually create, start, and join every thread.
"""

from concurrent.futures import ThreadPoolExecutor
import time


def process_task(task_id):
    print(f"Processing task {task_id}")
    time.sleep(1)
    return f"Task {task_id} completed"


# max_workers=3 means only 3 threads will run at a time.
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(process_task, range(1, 8))

# executor.map returns results in the same order as input.
for result in results:
    print(result)
