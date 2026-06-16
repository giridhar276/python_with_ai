"""
Example 05: Timeout handling.

Concepts:
- Always use timeout in production code.
- timeout=(connect_timeout, read_timeout)
- Handle requests.exceptions.Timeout
"""

import requests

url = "https://fakestoreapi.com/products"

try:
    response = requests.get(
        url,
        timeout=(3, 10)  # 3 sec connect timeout, 10 sec read timeout
    )
    response.raise_for_status()
    print(response.json()[:2])

except requests.exceptions.Timeout:
    print("Request timed out. Server may be slow or network may be unstable.")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)

except requests.exceptions.RequestException as e:
    print("General request error:", e)
