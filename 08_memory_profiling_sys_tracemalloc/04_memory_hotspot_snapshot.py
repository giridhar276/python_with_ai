# Topic: Memory Profiling
# Example: Memory hotspot snapshot

import tracemalloc

tracemalloc.start()

data_1 = [x for x in range(50000)]
data_2 = [x * x for x in range(100000)]

# take_snapshot() captures memory allocation details.
snapshot = tracemalloc.take_snapshot()

# statistics() groups memory usage by line number.
top_stats = snapshot.statistics("lineno")

for stat in top_stats[:5]:
    print(stat)

tracemalloc.stop()
