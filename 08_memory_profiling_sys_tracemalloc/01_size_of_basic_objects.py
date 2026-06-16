# Topic: Memory Profiling
# Example: Object size

import sys

number = 100
text = "Python training"
items = [1, 2, 3, 4, 5]

# getsizeof() returns the memory size of the object container.
print(sys.getsizeof(number))
print(sys.getsizeof(text))
print(sys.getsizeof(items))
