# Topic: Large File Handling
# Example: gzip compression

import os
import gzip

input_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "large_text.txt")
compressed_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "large_text.txt.gz")

os.makedirs(os.path.dirname(input_file), exist_ok=True)

with open(input_file, "w", encoding="utf-8") as file:
    file.write("Python training\n" * 10000)

with open(input_file, "rb") as src:
    with gzip.open(compressed_file, "wb") as dest:
        dest.writelines(src)

print(compressed_file)
