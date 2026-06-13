import requests


def get_temperature(city):

    geo_url = (
        f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    )

    geo_response = requests.get(geo_url)

    geo_data = geo_response.json()

    if "results" not in geo_data:
        return "City Not Found"

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m,weather_code"
    )

    weather_response = requests.get(weather_url)

    weather_data = weather_response.json()

    current = weather_data["current"]

    return {
    "temperature": f"{current['temperature_2m']}°C",
    "wind_speed": f"{current['wind_speed_10m']} km/h",
    "weather_code": current["weather_code"]
    }