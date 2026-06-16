"""
Multiprocessing Example 13: Parallel Data Cleaning

Use Case:
Clean large datasets in parallel.
"""

from concurrent.futures import ProcessPoolExecutor


def clean_name(name):
    # Remove spaces and convert to title case.
    return name.strip().title()


if __name__ == "__main__":
    names = [" asha ", " RAVI", "meera  ", "JOHN", " kavya"]

    with ProcessPoolExecutor(max_workers=3) as executor:
        cleaned_names = list(executor.map(clean_name, names))

    print(cleaned_names)
