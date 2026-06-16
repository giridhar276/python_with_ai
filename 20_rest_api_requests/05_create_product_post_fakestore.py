import requests

# POST is used to create/send new data to an API.
# json=payload automatically serializes the Python dict into JSON.
# headers are used to send extra request metadata.

URL = "https://fakestoreapi.com/products"

payload = {
    "title": "Training Laptop Bag",
    "price": 49.99,
    "description": "A sample product created from Python requests.",
    "image": "https://example.com/bag.png",
    "category": "electronics"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

try:
    response = requests.post(URL, json=payload, headers=headers, timeout=10)
    response.raise_for_status()

    print("Status Code:", response.status_code)
    print("Created Product:", response.json())

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
