"""
Threading Example 7: Web Scraping with Threading

Real-time Use Case:
Scrape multiple web pages faster using threads.

Install:
pip install requests beautifulsoup4
"""

from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup


urls = [
    "https://example.com",
    "https://httpbin.org/html",
]


def scrape_title(url):
    # Download page HTML.
    response = requests.get(url, timeout=10)

    # Parse HTML using BeautifulSoup.
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract title if available.
    title = soup.title.string.strip() if soup.title else "No title found"

    return url, title


with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(scrape_title, urls)

for url, title in results:
    print(f"{url} -> {title}")
