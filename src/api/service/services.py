import requests
from fastapi import FastAPI, HTTPException
class Service:
    """Service class has two methods {getWeatherByCity} and {getWeatherByGeolocation} these two methods are use for two end point /v1/weather/city_name and v2/weather/geolocation."""
    
    def __init__(self):
        print("Service initiated")
        self.token ="086368406f95097df8d0f36099304a44"
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        
    
    def getWeatherByCity(self, city):
        """ this method will accept a city params and return creturn a weather object
        :city will be a string value
        """
        url = "{0}?q={1}&appid={2}".format(self.base_url, city, self.token)
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        if not response:
          raise HTTPException(status_code=404, detail="Something went wrong!!")
        return response.json()
    
    def getWeatherByGeolocation(self, prop):
        """ this method will accept longitude and latitude and return a weather object
        :longitude this will a float value representing
        :latitude this will a float value representing
        """
        url = "{0}?lat={1}&lon={2}&appid={3}".format(self.base_url, prop.latitude, prop.longitude, self.token)
        payload={}
        headers = {}
        print('url', url)
        response = requests.request("GET", url, headers=headers, data=payload)
        if not response:
          raise HTTPException(status_code=404, detail="Something went wrong!!")
        return response.json()
