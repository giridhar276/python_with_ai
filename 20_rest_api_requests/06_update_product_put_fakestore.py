import requests

# PUT is used to fully update/replace a resource.
# Usually, the full object is sent in the request body.

PRODUCT_ID = 7
URL = f"https://fakestoreapi.com/products/{PRODUCT_ID}"

updated_product = {
    "title": "Updated Training Product",
    "price": 99.99,
    "description": "Fully updated product using PUT.",
    "image": "https://example.com/updated.png",
    "category": "electronics"
}

try:
    response = requests.put(URL, json=updated_product, timeout=10)
    response.raise_for_status()

    print("Status Code:", response.status_code)
    print("Updated Product:", response.json())

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
