from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "ERUBE AI Director"

    APP_ENV: str = "development"

    DEBUG: bool = True

    API_V1_PREFIX: str = "/api/v1"

    DJANGO_API_URL: str = "http://django:8000"

    REDIS_URL: str = "redis://redis:6379/0"

    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()