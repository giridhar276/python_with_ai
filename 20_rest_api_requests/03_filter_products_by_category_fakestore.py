import requests

# This example filters products by category.
# The category is part of the URL path.

CATEGORY = "jewelery"
URL = f"https://fakestoreapi.com/products/category/{CATEGORY}"

try:
    response = requests.get(URL, timeout=10)

    # headers contains response metadata such as Content-Type.
    print("Content-Type:", response.headers.get("Content-Type"))

    response.raise_for_status()

    products = response.json()

    for item in products:
        print(f"- {item['title']} | ${item['price']}")

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
