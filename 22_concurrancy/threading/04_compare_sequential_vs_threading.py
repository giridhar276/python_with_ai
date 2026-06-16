"""
Threading Example 4: Sequential vs Threading Timing

Concept:
Threading can reduce total waiting time for I/O-bound tasks.

This example compares:
1. Sequential execution
2. Threaded execution
"""

import threading
import time


def api_like_task(task_name):
    print(f"{task_name} started")
    time.sleep(2)
    print(f"{task_name} completed")


# Sequential execution
start = time.time()
api_like_task("Task 1")
api_like_task("Task 2")
sequential_time = time.time() - start

print("Sequential time:", round(sequential_time, 2), "seconds")

# Threaded execution
start = time.time()

thread1 = threading.Thread(target=api_like_task, args=("Thread Task 1",))
thread2 = threading.Thread(target=api_like_task, args=("Thread Task 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

threaded_time = time.time() - start
print("Threaded time:", round(threaded_time, 2), "seconds")
