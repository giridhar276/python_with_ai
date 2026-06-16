"""
Threading Example 1: Basic Thread

Concept:
A thread is a small unit of execution inside a process.
In Python, we use the threading module to create and manage threads.

Use Case:
When one task is waiting, another task can continue running.
"""

import threading
import time


def simple_task():
    # This function will run inside a separate thread.
    print("Thread task started")

    # sleep() simulates a slow task such as reading a file or waiting for an API response.
    time.sleep(2)

    print("Thread task completed")


# Create a Thread object.
# target=simple_task means this function will be executed by the thread.
thread = threading.Thread(target=simple_task)

# start() starts the thread execution.
thread.start()

# join() tells the main program to wait until this thread finishes.
thread.join()

print("Main program completed")
