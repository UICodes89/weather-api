from fastapi import APIRouter


from ...service.services import Service
from ...models.weather import city, geolocation

router = APIRouter()
service = Service()

@router.get("/weather/{city}", tags=["weather"])
async def weatherUsingCity(city: str):
    """this is a post method, and will accept one prameter
    :city this will be a string type value
    """
    print(city)
    return service.getWeatherByCity(city)

@router.post("/weather/", tags=["weather"])
async def weatherUsingGeolocation(prop:geolocation):
    """ this method will be search weather based on geolocation, it will accept a prop whihc will hold longitude and latitude
    :latitude this will be a float value
    :longitude this will be a float value
    """
    return service.getWeatherByGeolocation(prop) 
