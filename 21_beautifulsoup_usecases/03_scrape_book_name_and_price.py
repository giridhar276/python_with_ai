"""
Example 3: Scrape Book Name and Price

Use case:
Extract product names and prices from a website.

Website:
https://books.toscrape.com/

Required libraries:
pip install requests beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"

# Send GET request to website.
response = requests.get(url, timeout=10)

# Convert HTML into BeautifulSoup object.
soup = BeautifulSoup(response.text, "html.parser")

# Each product card is stored inside article tag with class product_pod.
articles = soup.find_all("article", class_="product_pod")

for article in articles:
    # Extract book name.
    book_name = article.find("h3").find("a")["title"]

    # Extract price.
    price = article.find("p", class_="price_color").text

    print("Book Name:", book_name)
    print("Price:", price)
    print("-" * 40)
