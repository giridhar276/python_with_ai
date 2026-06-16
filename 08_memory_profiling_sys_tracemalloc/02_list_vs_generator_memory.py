# Topic: Memory Profiling
# Example: List vs generator

import sys

numbers_list = [num for num in range(100000)]
numbers_generator = (num for num in range(100000))

print("List memory:", sys.getsizeof(numbers_list))
print("Generator memory:", sys.getsizeof(numbers_generator))
