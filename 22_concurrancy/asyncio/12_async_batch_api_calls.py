"""
Asyncio Example 14: Batch API Calls

Real-time Use Case:
Call APIs in controlled batches.

Install:
pip install aiohttp
"""

import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url, timeout=10) as response:
        return url, response.status


async def main():
    urls = ["https://httpbin.org/get"] * 10
    batch_size = 3

    async with aiohttp.ClientSession() as session:
        for index in range(0, len(urls), batch_size):
            batch = urls[index:index + batch_size]

            results = await asyncio.gather(*(fetch(session, url) for url in batch))
            print("Batch result:", results)


asyncio.run(main())
