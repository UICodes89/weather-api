from fastapi import Depends, FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from api.v1.endpoints import weather

import sys
import os
sys.path.append(os.pardir)
sys.path.append(os.path.join(os.pardir, os.pardir))

import uvicorn
async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(str(exc), status_code=400)


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Weather API",
        version="2.5.0",
        description="This is an API to check wehtehr based on city and geolocation",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

#Including routes
app.include_router(weather.router,prefix="/api/v1")


@app.get("/health")
async def root():
    """End point will return status of api 200 if api is up and runing and functioning correctly"""
    return {
        'code':200, 'status':'ok'
    }
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8005)
    print("running")