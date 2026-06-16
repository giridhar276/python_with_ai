import requests

# This example fetches hourly weather forecast.
# It is useful to explain nested JSON and list processing.

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 12.9716,
    "longitude": 77.5946,
    "hourly": "temperature_2m,precipitation_probability",
    "forecast_days": 1,
    "timezone": "Asia/Kolkata"
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    times = data["hourly"]["time"]
    temperatures = data["hourly"]["temperature_2m"]
    rain_probabilities = data["hourly"]["precipitation_probability"]

    for time, temp, rain in zip(times[:8], temperatures[:8], rain_probabilities[:8]):
        print(f"{time} | Temp: {temp}°C | Rain Probability: {rain}%")

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
