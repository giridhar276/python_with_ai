"""
Threading Example 11: Lock Solution

Concept:
threading.Lock is used to protect shared data.

Only one thread can enter the lock block at a time.
"""

import threading


counter = 0
lock = threading.Lock()


def increment_counter():
    global counter

    for _ in range(100000):
        # with lock ensures only one thread updates counter at a time.
        with lock:
            counter += 1


threads = []

for _ in range(5):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Final counter value:", counter)
print("Expected counter value:", 500000)
