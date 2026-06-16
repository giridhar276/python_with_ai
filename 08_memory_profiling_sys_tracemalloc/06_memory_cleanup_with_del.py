# Topic: Memory Profiling
# Example: Memory cleanup

import tracemalloc

tracemalloc.start()

large_data = [x for x in range(100000)]

print("Before delete:", tracemalloc.get_traced_memory())

del large_data

print("After delete:", tracemalloc.get_traced_memory())

tracemalloc.stop()
