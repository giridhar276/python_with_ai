"""
Example 5: Scrape Multiple Pages

Use case:
Scrape data from paginated websites.

Website:
https://books.toscrape.com/

Required libraries:
pip install requests beautifulsoup4 pandas
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


# Dynamic URL where page number changes.
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

# Scrape pages 1 to 5.
for page_number in range(1, 6):
    url = base_url.format(page_number)

    print("Scraping:", url)

    # Download current page.
    response = requests.get(url, timeout=10)

    # Parse HTML.
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract product cards.
    articles = soup.find_all("article", class_="product_pod")

    for article in articles:
        book_name = article.find("h3").find("a")["title"]
        price = article.find("p", class_="price_color").text
        availability = article.find("p", class_="instock availability").text.strip()

        all_books.append({
            "Book Name": book_name,
            "Price": price,
            "Availability": availability,
            "Page Number": page_number
        })

# Convert to DataFrame and save.
df = pd.DataFrame(all_books)

df.to_csv("multiple_pages_books.csv", index=False)

print("Scraping completed.")
print("Total books scraped:", len(df))
print(df.head())
