"""
Example 07: Retries and exponential backoff.

Concepts:
- requests.Session()
- HTTPAdapter
- urllib3.util.retry.Retry
- Retry on 429, 500, 502, 503, 504
- Backoff strategy

Important:
Retry POST/PATCH carefully because they may not be idempotent.
"""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_retry_session() -> requests.Session:
    retry_strategy = Retry(
        total=3,
        connect=3,
        read=3,
        status=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD", "OPTIONS"],
        respect_retry_after_header=True,
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)

    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    return session

session = create_retry_session()

try:
    response = session.get("https://fakestoreapi.com/products", timeout=10)
    response.raise_for_status()
    print("Success:", len(response.json()), "products received")

except requests.exceptions.RetryError as e:
    print("Retry attempts exhausted:", e)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)

finally:
    session.close()
