import requests

class Service:
    
    def __init__(self):
        print("Service initiatedd")
        self.token ="086368406f95097df8d0f36099304a44"
    
    
    def getWeatherByCity(self, city):
        url = "https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}".format(city, self.token)
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)
        return response.json()
    
    def getWeatherByGeolocation(self, longitude, latitude):
        url = "https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}".format(city, self.token)
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)
        return response.json()

