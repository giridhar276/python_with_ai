import requests

# Open-Meteo is a weather API.
# params is used to send query parameters cleanly instead of manually building a long URL.

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 17.3850,
    "longitude": 78.4867,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "Asia/Kolkata"
}

try:
    response = requests.get(URL, params=params, timeout=10)

    # response.url shows the final URL created by requests with query parameters.
    print("Final URL:", response.url)

    response.raise_for_status()

    data = response.json()
    current = data["current"]
    units = data["current_units"]

    print("Time:", current["time"])
    print("Temperature:", current["temperature_2m"], units["temperature_2m"])
    print("Humidity:", current["relative_humidity_2m"], units["relative_humidity_2m"])
    print("Wind Speed:", current["wind_speed_10m"], units["wind_speed_10m"])

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
