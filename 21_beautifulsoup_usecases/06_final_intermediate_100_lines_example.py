"""
Final BeautifulSoup Real-Time Example
-------------------------------------

Use case:
Scrape multiple pages of book data from an e-commerce-style website,
clean the data, save it into CSV, and display a small summary.

Website used:
https://books.toscrape.com/

Install required libraries:
pip install requests beautifulsoup4 pandas
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# ---------------------------------------------------------
# Function 1: Download HTML content from a webpage
# ---------------------------------------------------------
def get_html(url):
    """
    This function sends a GET request to the given URL
    and returns the HTML content if the request is successful.
    """

    try:
        response = requests.get(url, timeout=10)

        # Raise error if status code is 4xx or 5xx.
        response.raise_for_status()

        return response.text

    except requests.exceptions.RequestException as error:
        print("Error while downloading page:", url)
        print("Reason:", error)
        return None


# ---------------------------------------------------------
# Function 2: Convert rating text into number
# ---------------------------------------------------------
def convert_rating_to_number(rating_text):
    """
    The website stores ratings as text like:
    One, Two, Three, Four, Five

    This function converts them into numbers.
    """

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    return rating_map.get(rating_text, 0)


# ---------------------------------------------------------
# Function 3: Extract book details from one page
# ---------------------------------------------------------
def scrape_books_from_page(url, page_number):
    """
    This function scrapes all books from a single page.
    It returns a list of dictionaries.
    """

    html_content = get_html(url)

    if html_content is None:
        return []

    soup = BeautifulSoup(html_content, "html.parser")

    book_cards = soup.find_all("article", class_="product_pod")

    books = []

    for card in book_cards:
        # Book title
        title_tag = card.find("h3").find("a")
        book_title = title_tag["title"]

        # Book URL
        relative_link = title_tag["href"]
        book_url = "https://books.toscrape.com/catalogue/" + relative_link.replace("../", "")

        # Price
        price_text = card.find("p", class_="price_color").text
        cleaned_price = price_text.replace("£", "").strip()
        price = float(cleaned_price)

        # Availability
        availability = card.find("p", class_="instock availability").text.strip()

        # Rating
        rating_tag = card.find("p", class_="star-rating")
        rating_text = rating_tag["class"][1]
        rating_number = convert_rating_to_number(rating_text)

        # Store extracted data
        books.append({
            "Page Number": page_number,
            "Book Title": book_title,
            "Price": price,
            "Availability": availability,
            "Rating Text": rating_text,
            "Rating Number": rating_number,
            "Book URL": book_url
        })

    return books


# ---------------------------------------------------------
# Function 4: Scrape multiple pages
# ---------------------------------------------------------
def scrape_multiple_pages(total_pages):
    """
    This function loops through multiple pages
    and collects all book data.
    """

    all_books = []

    for page_number in range(1, total_pages + 1):
        page_url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"

        print(f"Scraping page {page_number}: {page_url}")

        books = scrape_books_from_page(page_url, page_number)

        all_books.extend(books)

        # Small delay to avoid hitting the server too fast.
        time.sleep(1)

    return all_books


# ---------------------------------------------------------
# Function 5: Save data and display summary
# ---------------------------------------------------------
def save_and_summarize(book_data):
    """
    This function converts scraped data into a DataFrame,
    saves it to CSV, and displays useful summary information.
    """

    if not book_data:
        print("No data found.")
        return

    df = pd.DataFrame(book_data)

    df.to_csv("final_books_scraping_output.csv", index=False)

    print("\nData saved successfully.")
    print("File name: final_books_scraping_output.csv")

    print("\nFirst 5 Records:")
    print(df.head())

    print("\nSummary:")
    print("Total books scraped:", len(df))
    print("Average price:", round(df["Price"].mean(), 2))
    print("Minimum price:", df["Price"].min())
    print("Maximum price:", df["Price"].max())

    print("\nBooks by Rating:")
    print(df["Rating Number"].value_counts().sort_index())

    print("\nTop 5 Costliest Books:")
    print(df.sort_values(by="Price", ascending=False)[["Book Title", "Price", "Rating Number"]].head())


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------
if __name__ == "__main__":

    print("BeautifulSoup Final Web Scraping Example Started")
    print("-" * 60)

    total_pages_to_scrape = 5

    scraped_books = scrape_multiple_pages(total_pages_to_scrape)

    save_and_summarize(scraped_books)

    print("-" * 60)
    print("BeautifulSoup Final Web Scraping Example Completed")
