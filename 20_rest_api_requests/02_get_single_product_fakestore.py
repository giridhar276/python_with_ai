import requests

# Path parameter example:
# The product id is passed directly in the URL.

PRODUCT_ID = 1
URL = f"https://fakestoreapi.com/products/{PRODUCT_ID}"

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    product = response.json()

    print("Title:", product["title"])
    print("Price:", product["price"])
    print("Category:", product["category"])
    print("Rating:", product["rating"]["rate"])

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
