# Topic: Memory Profiling
# Example: Current and peak memory

import tracemalloc

# tracemalloc.start() starts memory tracking.
tracemalloc.start()

data = [num * 2 for num in range(100000)]

# get_traced_memory() returns current and peak memory usage.
current, peak = tracemalloc.get_traced_memory()

print(current, peak)

# tracemalloc.stop() stops memory tracking.
tracemalloc.stop()
