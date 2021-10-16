from fastapi import FastAPI
from fastapi.testclient import TestClient 
from src.main import app
app = FastAPI()
client = TestClient(app)
city = "cork"
sucess_response = {
    "coord": {
        "lon": -8.4706,
        "lat": 51.898
    },
    "weather": [
        {
            "id": 803,
            "main": "Clouds",
            "description": "broken clouds",
            "icon": "04n"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 286.13,
        "feels_like": 285.7,
        "temp_min": 285.4,
        "temp_max": 286.28,
        "pressure": 1027,
        "humidity": 85
    },
    "visibility": 10000,
    "wind": {
        "speed": 2.06,
        "deg": 180
    },
    "clouds": {
        "all": 75
    },
    "dt": 1634157097,
    "sys": {
        "type": 1,
        "id": 1563,
        "country": "IE",
        "sunrise": 1634108097,
        "sunset": 1634147094
    },
    "timezone": 3600,
    "id": 2965140,
    "name": "Cork",
    "cod": 200
}

def test_read_root():
    response = client.get('/api/v1/weather/{0}'.format(city))
    assert response.status_code == 200
    
def test_read_root():
    response = client.get('/api/v1/weather/{0}'.format(''))
    assert response.status_code == 405

def test_read_root():
    response = client.get('/api/v1/weather/{0}'.format('sdgsd'))
    assert response.status_code == 404
    
    
    
    
#functional case for [/api/v1/weather/] body{latitude and longitude}
    
def test_read_root():
    response = client.post('/api/v1/weather/', headers={'Content-Type': 'application/json'}, json={"longitude": 53.3497645, "latitude": -6.2602732})
    assert response.status_code == 200
    
def test_read_root():
    response = client.post('/api/v1/weather/', headers={'Content-Type': 'application/json'}, json={"longitude": '', "latitude": ''})
    assert response.status_code == 404

def test_read_root():
    response = client.post('/api/v1/weather/', headers={'Content-Type': 'application/json'}, json={"longitude": 01.0, "latitude": -0.21})
    assert response.status_code == 200