"""
Asyncio Example 7: Async Web Scraping

Real-time Use Case:
Fetch multiple web pages asynchronously and extract titles.

Install:
pip install aiohttp beautifulsoup4
"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def get_title(session, url):
    async with session.get(url, timeout=10) as response:
        html = await response.text()

    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title else "No title"

    return url, title


async def main():
    urls = ["https://example.com", "https://httpbin.org/html"]

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(get_title(session, url) for url in urls))

    for url, title in results:
        print(url, "->", title)


asyncio.run(main())
