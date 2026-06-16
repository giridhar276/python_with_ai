"""
Example 03: PUT vs PATCH.

PUT:
- Usually replaces the complete resource.

PATCH:
- Usually updates only selected fields.

Note:
FakeStore API is a demo API. It simulates the response but may not permanently save changes.
"""

import requests

url = "https://fakestoreapi.com/products/1"

put_payload = {
    "title": "Completely Replaced Product",
    "price": 999,
    "description": "Full product replacement",
    "category": "electronics",
    "image": "https://example.com/full.png"
}

patch_payload = {
    "price": 799
}

put_response = requests.put(url, json=put_payload, timeout=10)
put_response.raise_for_status()

print("PUT Response:")
print(put_response.json())

patch_response = requests.patch(url, json=patch_payload, timeout=10)
patch_response.raise_for_status()

print("\nPATCH Response:")
print(patch_response.json())
