from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello Weather App"}


@app.get("/greet")
def greet(name: str):
    @app.get("/weather")
    def weather(city: str):
        return {
            "city": city,
            "temperature": "32°C"
        }