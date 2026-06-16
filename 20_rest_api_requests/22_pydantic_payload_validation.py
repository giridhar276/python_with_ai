"""
Example 09: Payload validation using Pydantic.

Concepts:
- Pydantic BaseModel
- Field constraints
- model_dump()
- Validate data before sending API request
"""

import requests
from pydantic import BaseModel, Field, ValidationError

class ProductCreateRequest(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    price: float = Field(gt=0)
    description: str = Field(min_length=5)
    category: str
    image: str

payload = {
    "title": "Python API Course",
    "price": 999.0,
    "description": "REST API course product",
    "category": "training",
    "image": "https://example.com/course.png"
}

try:
    validated_payload = ProductCreateRequest.model_validate(payload)

    response = requests.post(
        "https://fakestoreapi.com/products",
        json=validated_payload.model_dump(),
        timeout=10
    )

    response.raise_for_status()
    print("Validated and submitted successfully")
    print(response.json())

except ValidationError as e:
    print("Payload validation failed:")
    print(e)

except requests.exceptions.RequestException as e:
    print("API request failed:", e)
