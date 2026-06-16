import requests

# Session is useful when multiple requests share the same headers or connection.
# It can improve performance when calling many APIs from the same host.

BASE_URL = "https://restcountries.com/v3.1"

session = requests.Session()
session.headers.update({
    "Accept": "application/json"
})

params = {
    "fields": "name,capital,population,region,currencies,languages"
}

try:
    response = session.get(f"{BASE_URL}/name/india", params=params, timeout=10)
    response.raise_for_status()

    countries = response.json()

    for country in countries:
        print("Country:", country["name"]["common"])
        print("Capital:", country.get("capital", ["N/A"])[0])
        print("Region:", country.get("region"))
        print("Population:", country.get("population"))
        print("Currencies:", list(country.get("currencies", {}).keys()))
        print("Languages:", list(country.get("languages", {}).values()))

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
