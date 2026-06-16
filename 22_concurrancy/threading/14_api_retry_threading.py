"""
Threading Example 14: API Retry with Threading

Real-time Use Case:
Call multiple APIs with retry logic.

Install:
pip install requests
"""

from concurrent.futures import ThreadPoolExecutor
import requests
import time


urls = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/1",
]


def fetch_with_retry(url, retries=3):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                return url, "SUCCESS"

            print(f"{url} failed with status {response.status_code}, attempt {attempt}")

        except requests.RequestException as error:
            print(f"{url} failed with error {error}, attempt {attempt}")

        # Wait before retrying.
        time.sleep(1)

    return url, "FAILED"


with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(fetch_with_retry, urls)

for result in results:
    print(result)
