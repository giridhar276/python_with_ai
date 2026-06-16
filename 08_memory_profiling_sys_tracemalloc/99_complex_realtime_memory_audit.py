# Topic: Complex Memory Profiling
# Example: Memory audit for data processing

import sys
import tracemalloc

tracemalloc.start()

raw_records = [{"id": i, "amount": i * 10} for i in range(100000)]
filtered_records = [row for row in raw_records if row["amount"] > 500000]

current, peak = tracemalloc.get_traced_memory()

print("Raw list size:", sys.getsizeof(raw_records))
print("Filtered records:", len(filtered_records))
print("Current memory:", current)
print("Peak memory:", peak)

tracemalloc.stop()
