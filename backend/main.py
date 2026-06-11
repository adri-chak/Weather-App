from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello Weather App"}


@app.get("/greet")
def greet(name: str):
    @app.get("/weather")
    def weather(city: str):

        weather_data = {
            "Kolkata": "32°C",
            "Delhi": "38°C",
            "Mumbai": "30°C",
            "Bangalore": "27°C"
        }

        return {
            "city": city,
            "temperature": weather_data.get(city, "Data Not Available")
        }