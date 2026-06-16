# Topic: Third-party Libraries
# Example: tqdm progress bar

try:
    from tqdm import tqdm
except ImportError:
    print("Please install tqdm: pip install tqdm")
    raise SystemExit

import time

# tqdm() displays progress bar for an iterable.
for item in tqdm(range(20), desc="Processing records"):
    time.sleep(0.05)
