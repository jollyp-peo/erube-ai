from fastapi import FastAPI

from app.api.routes import router
from app.core.settings import settings
from app.core.logging import configure_logging


logger = configure_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
)

app.include_router(
    router,
    prefix=settings.API_V1_PREFIX,
)


@app.get("/")
async def root():

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