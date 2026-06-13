from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from backend.api.weather import get_temperature

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

    return {
        "city": city,
        "temperature": get_temperature(city)
    }

@app.get("/test")
def test():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/1"
    )

    return response.json()

    return {
        "city": city,
        "temperature": weather_data.get(city, "Data Not Available")
    }