"""
Asyncio Example 6: aiohttp GET Requests

Concept:
aiohttp is a true asynchronous HTTP client.

Install:
pip install aiohttp
"""

import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url, timeout=10) as response:
        text = await response.text()
        return url, response.status, len(text)


async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/ip",
        "https://httpbin.org/uuid",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for url, status, length in results:
        print(url, status, length)


asyncio.run(main())
