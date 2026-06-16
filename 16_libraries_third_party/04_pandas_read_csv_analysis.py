# Topic: Third-party Libraries
# Example: pandas CSV analysis

import os

try:
    import pandas as pd
except ImportError:
    print("Please install pandas: pip install pandas")
    raise SystemExit

file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "employees.csv")

# read_csv() loads CSV data into a DataFrame.
df = pd.read_csv(file_path)

# groupby() groups rows by department.
print(df.groupby("department")["salary"].mean())
