"""
Threading Example 12: Queue with Worker Threads

Concept:
queue.Queue is thread-safe.
It is useful when multiple worker threads need to process tasks from a common queue.

Real-time Use Case:
Background job processing, file processing, email sending, log processing.
"""

import queue
import threading
import time


task_queue = queue.Queue()


def worker(worker_name):
    while True:
        # get() waits until a task is available.
        task = task_queue.get()

        # None is used as a stop signal.
        if task is None:
            task_queue.task_done()
            print(f"{worker_name} stopped")
            break

        print(f"{worker_name} processing {task}")
        time.sleep(1)

        # Mark this task as completed.
        task_queue.task_done()


workers = []

for i in range(3):
    thread = threading.Thread(target=worker, args=(f"Worker-{i+1}",))
    thread.start()
    workers.append(thread)

# Add tasks to the queue.
for task_id in range(1, 8):
    task_queue.put(f"Task-{task_id}")

# Wait until all tasks are completed.
task_queue.join()

# Send stop signal to each worker.
for _ in workers:
    task_queue.put(None)

for thread in workers:
    thread.join()

print("All queue tasks completed")
