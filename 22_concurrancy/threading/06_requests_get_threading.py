"""
Threading Example 6: requests.get with Threading

Real-time Use Case:
Calling multiple REST APIs concurrently.

Why threading?
requests.get() is blocking. While one request waits for server response,
another thread can start another request.

Install:
pip install requests
"""

from concurrent.futures import ThreadPoolExecutor
import requests


urls = [
    "https://httpbin.org/get",
    "https://httpbin.org/ip",
    "https://httpbin.org/uuid",
]


def fetch_url(url):
    # timeout prevents the request from waiting forever.
    response = requests.get(url, timeout=10)

    # Return useful information from the API call.
    return {
        "url": url,
        "status_code": response.status_code,
        "response_length": len(response.text)
    }


with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(fetch_url, urls)

for result in results:
    print(result)
