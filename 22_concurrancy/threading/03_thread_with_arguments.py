"""
Threading Example 3: Passing Arguments to a Thread

Concept:
args is used to pass values to the target function.

Important:
args must be a tuple. For one argument, use args=(value,)
"""

import threading


def greet_student(name, topic):
    # This function accepts two arguments.
    print(f"Hello {name}, today we are learning {topic}")


thread = threading.Thread(
    target=greet_student,
    args=("Asha", "Python Threading")
)

thread.start()
thread.join()
