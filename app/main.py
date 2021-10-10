from fastapi import Depends, FastAPI

from .core.dependencies import get_query_token, get_token_header
from .routers import weather

app = FastAPI()
app.include_router(weather.router)


@app.get("/health")
async def root():
    return {
        'code':200, 'status':'ok'
    }
