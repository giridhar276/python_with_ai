"""
Example 06: Session reuse.

Concepts:
- requests.Session()
- common headers
- common base settings
- connection pooling/reuse
"""

import requests

session = requests.Session()

session.headers.update({
    "Accept": "application/json",
    "User-Agent": "TrainingSessionClient/1.0"
})

base_url = "https://fakestoreapi.com"

response1 = session.get(f"{base_url}/products", params={"limit": 3}, timeout=10)
response1.raise_for_status()

response2 = session.get(f"{base_url}/products/categories", timeout=10)
response2.raise_for_status()

print("Products:")
for product in response1.json():
    print(product["title"])

print("\nCategories:")
print(response2.json())

session.close()
