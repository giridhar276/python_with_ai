import requests

# GET is used to read/fetch data from a REST API.
# This API returns a list of products in JSON format.

URL = "https://fakestoreapi.com/products"

try:
    response = requests.get(URL, timeout=10)

    # status_code tells whether the request succeeded or failed.
    print("Status Code:", response.status_code)

    # raise_for_status() raises an error for 4xx/5xx responses.
    response.raise_for_status()

    # json() converts JSON response into Python list/dictionary.
    products = response.json()

    print("Total Products:", len(products))

    for product in products[:5]:
        print(f"{product['id']}. {product['title']} - ${product['price']}")

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
