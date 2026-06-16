# Topic: Context Manager
# Example: contextlib timer

from contextlib import contextmanager
import time

# contextmanager allows creating a context manager using a function.
@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print("Time taken:", round(end - start, 4), "seconds")

with timer():
    numbers = [x for x in range(100000)]
