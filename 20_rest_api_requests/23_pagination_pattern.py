"""
Example 10: Pagination pattern.

Concepts:
- page number
- limit/page size
- loop until no more data
- generator function

This example uses JSONPlaceholder for pagination demo because it supports _page and _limit.
"""

import requests

def fetch_paginated_posts(page_size=10, max_pages=3):
    base_url = "https://jsonplaceholder.typicode.com/posts"
    page = 1

    while page <= max_pages:
        response = requests.get(
            base_url,
            params={"_page": page, "_limit": page_size},
            timeout=10
        )
        response.raise_for_status()

        items = response.json()

        if not items:
            break

        yield page, items
        page += 1

for page, posts in fetch_paginated_posts():
    print(f"\nPage {page}")
    for post in posts:
        print(post["id"], post["title"])
