"""
Example 4: Scrape Books and Save to CSV

Use case:
Scrape book data and store it for later analysis.

Website:
https://books.toscrape.com/

Required libraries:
pip install requests beautifulsoup4 pandas
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://books.toscrape.com/"

# Download webpage.
response = requests.get(url, timeout=10)

# Parse webpage.
soup = BeautifulSoup(response.text, "html.parser")

# Get all product cards.
articles = soup.find_all("article", class_="product_pod")

# Empty list to store scraped records.
book_data = []

for article in articles:
    # Extract book name.
    book_name = article.find("h3").find("a")["title"]

    # Extract price.
    price = article.find("p", class_="price_color").text

    # Extract availability and remove extra spaces/newlines.
    availability = article.find("p", class_="instock availability").text.strip()

    # Store each book as a dictionary.
    book_data.append({
        "Book Name": book_name,
        "Price": price,
        "Availability": availability
    })

# Convert list of dictionaries into DataFrame.
df = pd.DataFrame(book_data)

# Save data into CSV file.
df.to_csv("books_data.csv", index=False)

print("Data saved successfully to books_data.csv")
print(df.head())
