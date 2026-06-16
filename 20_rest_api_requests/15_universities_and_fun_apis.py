import requests

# This example shows two simple public APIs:
# 1. Universities API - search universities by country.
# 2. Dog CEO API - get a random dog image.
# It also demonstrates reusable API helper functions.

def get_json(url, **kwargs):
    """Reusable helper function for GET APIs."""
    response = requests.get(url, timeout=10, **kwargs)
    response.raise_for_status()
    return response.json()


try:
    universities_url = "http://universities.hipolabs.com/search"

    params = {
        "country": "India"
    }

    universities = get_json(universities_url, params=params)

    print("Sample Universities:")
    for university in universities[:5]:
        print("-", university["name"], "|", university.get("web_pages", ["N/A"])[0])

    dog_url = "https://dog.ceo/api/breeds/image/random"
    dog_data = get_json(dog_url)

    print("\nRandom Dog Image URL:")
    print(dog_data["message"])

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
