import requests

# This example uses Open-Meteo Air Quality API.
# It demonstrates a different API base URL but the same requests.get() pattern.

URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

params = {
    "latitude": 28.6139,
    "longitude": 77.2090,
    "hourly": "pm10,pm2_5,carbon_monoxide",
    "forecast_days": 1,
    "timezone": "Asia/Kolkata"
}

try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("Air Quality Sample for First 5 Hours:")
    for i in range(5):
        print(
            data["hourly"]["time"][i],
            "| PM10:", data["hourly"]["pm10"][i],
            "| PM2.5:", data["hourly"]["pm2_5"][i],
            "| CO:", data["hourly"]["carbon_monoxide"][i]
        )

except requests.exceptions.RequestException as error:
    print("API request failed:", error)
