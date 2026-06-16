import requests

# CoinGecko simple price API is useful for explaining real-world query parameters.
# We pass coin ids and currencies using params.

URL = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd,inr",
    "include_24hr_change": "true"
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    prices = response.json()

    for coin, details in prices.items():
        print("Coin:", coin)
        print("USD:", details.get("usd"))
        print("INR:", details.get("inr"))
        print("24h Change:", details.get("usd_24h_change"))
        print("-" * 30)

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
