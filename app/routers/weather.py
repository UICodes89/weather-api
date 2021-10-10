from fastapi import APIRouter
from ..service.service import Service
router = APIRouter()
service = Service()




@router.get("/weather/{city}", tags=["weather"])
async def read_weather_by_city(city: str):
    return service.getWeatherByCity(city)

@router.get("/weather/{longitude}/{latitude}", tags=["weather"])
async def read_weather_by_geolication(latitude: str, longitude: str):
    return service.getWeatherByCity(latitude, longitude)
