"""
Asyncio Example 5: requests.get using asyncio.to_thread

Concept:
requests is blocking, but asyncio.to_thread can run blocking code in a thread.

Install:
pip install requests
"""

import asyncio
import requests


def fetch_url(url):
    response = requests.get(url, timeout=10)
    return url, response.status_code


async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/ip",
        "https://httpbin.org/uuid",
    ]

    tasks = [asyncio.to_thread(fetch_url, url) for url in urls]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)


asyncio.run(main())
