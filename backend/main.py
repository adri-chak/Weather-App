from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello Weather App"}


@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}


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