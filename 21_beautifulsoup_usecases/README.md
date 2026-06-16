# BeautifulSoup Real-Time Examples

This ZIP contains 6 Python examples:

1. `01_scrape_page_title.py`
   - Scrapes the title of a webpage.

2. `02_extract_book_names.py`
   - Extracts all book names from the first page.

3. `03_scrape_book_name_and_price.py`
   - Extracts book names and prices.

4. `04_scrape_books_save_to_csv.py`
   - Extracts book details and saves them into CSV.

5. `05_scrape_multiple_pages.py`
   - Scrapes multiple pages and saves data into CSV.

6. `06_final_intermediate_100_lines_example.py`
   - Final intermediate-level project with functions, exception handling, pagination, cleaning, CSV export, and summary.

## Installation

Run this command before executing the scripts:

```bash
pip install requests beautifulsoup4 pandas
```

## How to Run

Example:

```bash
python 01_scrape_page_title.py
```

For the final example:

```bash
python 06_final_intermediate_100_lines_example.py
```

## Teaching Notes

These examples cover:

- `requests.get()`
- `BeautifulSoup()`
- `find()`
- `find_all()`
- Extracting text
- Extracting attributes
- CSS class-based scraping
- Data cleaning
- Pagination
- CSV export using Pandas
- Basic summary analysis

## Important Note

Always check a website's terms of service and `robots.txt` before scraping.
For production systems, prefer official APIs wherever available.
