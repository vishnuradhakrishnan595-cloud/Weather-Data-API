
from fastapi import FastAPI, HTTPException
import httpx

from app.services.weather_service import get_weather
from app.schemas import WeatherResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Weather Data API",
    description="Real-time weather information using OpenWeatherMap",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {
        "message": "Welcome to Weather Data API",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/weather/{city}", response_model=WeatherResponse)
async def weather(city: str):

    try:
        return await get_weather(city)

    except httpx.HTTPStatusError as error:

        if error.response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="City not found"
            )

        raise HTTPException(
            status_code=502,
            detail="Weather service error"
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Unable to connect to weather service"
        )
