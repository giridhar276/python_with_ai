"""
Example 01: GET request with headers and query parameters.

Concepts:
- requests.get()
- headers
- params
- status code
- JSON response parsing
"""

import requests

BASE_URL = "https://fakestoreapi.com/products"

headers = {
    "Accept": "application/json",
    "User-Agent": "PythonTrainingClient/1.0"
}

params = {
    "limit": 5
}

response = requests.get(
    BASE_URL,
    headers=headers,
    params=params,
    timeout=10
)

print("Final URL:", response.url)
print("Status Code:", response.status_code)

response.raise_for_status()

products = response.json()

for product in products:
    print(product["id"], product["title"], product["price"])
