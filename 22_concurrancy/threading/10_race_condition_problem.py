"""
Threading Example 10: Race Condition Problem

Concept:
A race condition happens when multiple threads modify shared data at the same time.

Expected:
If 5 threads each increment 100000 times, final value should be 500000.

But due to race condition, the result may be different.
"""

import threading


counter = 0


def increment_counter():
    global counter

    for _ in range(100000):
        # This operation is not fully safe between threads.
        # It involves read -> modify -> write.
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
