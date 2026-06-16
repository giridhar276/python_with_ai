"""
Example 08: Basic Auth and Bearer Token Auth.

Concepts:
- Basic Auth using auth=(username, password)
- Bearer token using Authorization header
- Environment variable usage
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Basic Auth style
basic_auth_url = "https://httpbin.org/basic-auth/demo/password"

try:
    basic_response = requests.get(
        basic_auth_url,
        auth=("demo", "password"),
        timeout=10
    )
    print("Basic Auth Status:", basic_response.status_code)
    print(basic_response.json())

except requests.exceptions.RequestException as e:
    print("Basic Auth request failed:", e)


# Bearer Token style
# In real projects, store token in .env:
# API_TOKEN=your_token_here
api_token = os.getenv("API_TOKEN", "sample-token-for-demo")

headers = {
    "Authorization": f"Bearer {api_token}",
    "Accept": "application/json"
}

try:
    response = requests.get(
        "https://httpbin.org/bearer",
        headers=headers,
        timeout=10
    )
    print("\nBearer Auth Status:", response.status_code)
    print(response.text)

except requests.exceptions.RequestException as e:
    print("Bearer Auth request failed:", e)
