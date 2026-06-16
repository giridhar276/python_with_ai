"""
Final Example: Reusable Session-Based API Client.

Concepts covered:
- Session-based API client
- headers
- params
- GET, POST, PUT, PATCH, DELETE
- retries and backoff
- timeout
- Pydantic validation
- logging and tracing
- centralized error handling
"""

import logging
import time
import uuid
from typing import Any, Optional

import requests
from pydantic import BaseModel, Field, ValidationError
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class ProductCreate(BaseModel):
    title: str = Field(min_length=3)
    price: float = Field(gt=0)
    description: str = Field(min_length=5)
    category: str
    image: str


class ProductPatch(BaseModel):
    title: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    description: Optional[str] = None
    category: Optional[str] = None
    image: Optional[str] = None


class APIClient:
    def __init__(
        self,
        base_url: str,
        token: Optional[str] = None,
        timeout: int = 10
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/json",
            "User-Agent": "ReusableTrainingAPIClient/1.0"
        })

        if token:
            self.session.headers.update({
                "Authorization": f"Bearer {token}"
            })

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
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def request(
        self,
        method: str,
        endpoint: str,
        params: Optional[dict] = None,
        json_body: Optional[dict] = None
    ) -> Any:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        correlation_id = str(uuid.uuid4())

        headers = {
            "X-Correlation-ID": correlation_id
        }

        start = time.perf_counter()

        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json_body,
                headers=headers,
                timeout=self.timeout
            )

            elapsed = time.perf_counter() - start

            logging.info(
                "method=%s url=%s status=%s duration=%.3fs correlation_id=%s",
                method,
                response.url,
                response.status_code,
                elapsed,
                correlation_id
            )

            response.raise_for_status()

            if response.text:
                return response.json()

            return None

        except requests.exceptions.Timeout:
            logging.exception("Timeout error correlation_id=%s", correlation_id)
            raise

        except requests.exceptions.HTTPError:
            logging.exception(
                "HTTP error status=%s body=%s correlation_id=%s",
                response.status_code,
                response.text,
                correlation_id
            )
            raise

        except requests.exceptions.RequestException:
            logging.exception("Request failed correlation_id=%s", correlation_id)
            raise

    def get(self, endpoint: str, params: Optional[dict] = None):
        return self.request("GET", endpoint, params=params)

    def post(self, endpoint: str, json_body: dict):
        return self.request("POST", endpoint, json_body=json_body)

    def put(self, endpoint: str, json_body: dict):
        return self.request("PUT", endpoint, json_body=json_body)

    def patch(self, endpoint: str, json_body: dict):
        return self.request("PATCH", endpoint, json_body=json_body)

    def delete(self, endpoint: str):
        return self.request("DELETE", endpoint)

    def close(self):
        self.session.close()


def main():
    client = APIClient(base_url="https://fakestoreapi.com")

    try:
        print("\n1. GET products")
        products = client.get("/products", params={"limit": 3})
        for product in products:
            print(product["id"], product["title"])

        print("\n2. POST create product with Pydantic validation")
        payload = ProductCreate.model_validate({
            "title": "Reusable API Client Course",
            "price": 1299,
            "description": "Advanced requests training",
            "category": "training",
            "image": "https://example.com/course.png"
        })

        created = client.post("/products", json_body=payload.model_dump())
        print(created)

        print("\n3. PATCH partial update with Pydantic validation")
        patch_payload = ProductPatch.model_validate({
            "price": 999
        })

        patched = client.patch(
            "/products/1",
            json_body=patch_payload.model_dump(exclude_none=True)
        )
        print(patched)

        print("\n4. DELETE product")
        deleted = client.delete("/products/1")
        print(deleted)

    except ValidationError as e:
        print("Validation failed:")
        print(e)

    finally:
        client.close()


if __name__ == "__main__":
    main()
