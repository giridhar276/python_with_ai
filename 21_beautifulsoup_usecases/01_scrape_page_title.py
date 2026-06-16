"""
Example 1: Scrape Page Title from a Website

Use case:
Check whether a website is reachable and extract its title.

Website:
https://books.toscrape.com/

Required libraries:
pip install requests beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"

# requests.get() sends a GET request to download the webpage content.
response = requests.get(url, timeout=10)

# BeautifulSoup converts HTML text into a searchable/parsing object.
soup = BeautifulSoup(response.text, "html.parser")

# soup.title gives the <title> tag, and .text extracts only text.
title = soup.title.text

print("Website Title:", title)
