
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List

class city(BaseModel):
    city: str

class geolocation(BaseModel):
    longitude: str
    latitude: str
