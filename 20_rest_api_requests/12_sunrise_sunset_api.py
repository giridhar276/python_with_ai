import requests

# Sunrise-Sunset API returns sunrise and sunset time based on latitude and longitude.
# This is a simple GET API with query parameters.

URL = "https://api.sunrise-sunset.org/json"

params = {
    "lat": 17.3850,
    "lng": 78.4867,
    "formatted": 0
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if data["status"] == "OK":
        results = data["results"]
        print("Sunrise:", results["sunrise"])
        print("Sunset:", results["sunset"])
        print("Day Length:", results["day_length"])
    else:
        print("API returned status:", data["status"])

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
