"""
Threading Example 2: Running Multiple Threads

Concept:
Multiple threads can be started to handle multiple I/O-bound tasks.

Use Case:
Downloading multiple files, calling multiple APIs, or reading multiple files.
"""

import threading
import time


def download_file(file_name):
    # Each thread receives a different file name.
    print(f"Starting download: {file_name}")

    # Simulate network delay.
    time.sleep(2)

    print(f"Completed download: {file_name}")


files = ["sales.csv", "employees.csv", "products.csv"]
threads = []

for file_name in files:
    # Create one thread per file.
    thread = threading.Thread(target=download_file, args=(file_name,))
    threads.append(thread)
    thread.start()

# Wait for every thread to complete.
for thread in threads:
    thread.join()

print("All downloads completed")
