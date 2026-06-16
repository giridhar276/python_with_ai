# Topic: Large File Handling
# Example: pandas chunks

import os

try:
    import pandas as pd
except ImportError:
    print("Please install pandas: pip install pandas")
    raise SystemExit

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs", "large_sales.csv")

if not os.path.exists(file_path):
    print("Run 01_generate_large_csv.py first")
else:
    # read_csv() with chunksize reads a large file in smaller parts.
    for chunk in pd.read_csv(file_path, chunksize=2000):
        print("Chunk rows:", len(chunk), "Total amount:", chunk["amount"].sum())
