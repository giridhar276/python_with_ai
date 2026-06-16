import requests

# response.ok is True for successful responses with status code below 400.

URL = "https://fakestoreapi.com/products/categories"

try:
    response = requests.get(URL, timeout=10)

    if response.ok:
        categories = response.json()
        print("Available Categories:")
        for category in categories:
            print("-", category)
    else:
        print("API failed with status:", response.status_code)

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
