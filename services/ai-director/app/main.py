from fastapi import FastAPI

from app.core.settings import settings
from app.core.logging import configure_logging


logger = configure_logging()


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
)


@app.get("/")
async def root():

    logger.info("AI Director Root Endpoint Hit")

    return {
        "service": settings.APP_NAME,
        "status": "healthy",
        "environment": settings.APP_ENV,
    }


@app.get("/health")
async def health():

    return {
        "status": "healthy",
    }