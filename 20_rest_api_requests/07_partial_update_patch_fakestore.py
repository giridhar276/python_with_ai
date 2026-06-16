import requests

# PATCH is used to partially update selected fields.
# Unlike PUT, we do not need to send the complete object.

PRODUCT_ID = 7
URL = f"https://fakestoreapi.com/products/{PRODUCT_ID}"

partial_update = {
    "price": 79.99,
    "title": "Partially Updated Product"
}

try:
    response = requests.patch(URL, json=partial_update, timeout=10)
    response.raise_for_status()

    print("Status Code:", response.status_code)
    print("Patched Product:", response.json())

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
