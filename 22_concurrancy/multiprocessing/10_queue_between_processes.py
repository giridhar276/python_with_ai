"""
Multiprocessing Example 10: Queue Between Processes

Concept:
Processes do not share memory directly.
Queue helps pass data between processes safely.
"""

import multiprocessing


def producer(queue):
    for number in range(1, 6):
        queue.put(number * number)


if __name__ == "__main__":
    queue = multiprocessing.Queue()

    process = multiprocessing.Process(target=producer, args=(queue,))
    process.start()
    process.join()

    while not queue.empty():
        print("Received from child process:", queue.get())
