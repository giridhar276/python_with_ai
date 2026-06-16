"""
Example 2: Extract All Book Names from a Web Page

Use case:
Scrape product/book names from an e-commerce-style page.

Website:
https://books.toscrape.com/

Required libraries:
pip install requests beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"

# Download page HTML.
response = requests.get(url, timeout=10)

# Parse HTML content.
soup = BeautifulSoup(response.text, "html.parser")

# Each book title is inside an <h3> tag.
books = soup.find_all("h3")

for book in books:
    # Inside h3, the <a> tag contains the title attribute.
    book_name = book.find("a")["title"]
    print(book_name)
