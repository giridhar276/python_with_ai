import requests

# DELETE is used to delete/remove a resource.
# Many demo APIs return a fake delete response without actually deleting data permanently.

PRODUCT_ID = 6
URL = f"https://fakestoreapi.com/products/{PRODUCT_ID}"

try:
    response = requests.delete(URL, timeout=10)
    response.raise_for_status()

    print("Status Code:", response.status_code)
    print("Deleted Product Response:", response.json())

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
