def get_temperature(city):

    weather_data = {
        "Kolkata": "32°C",
        "Delhi": "38°C",
        "Mumbai": "30°C",
        "Bangalore": "27°C"
    }

    return weather_data.get(city, "Data Not Available")