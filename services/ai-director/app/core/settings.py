from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "ERUBE AI Director"

    APP_ENV: str = "development"

    DEBUG: bool = True

    API_V1_PREFIX: str = "/api/v1"

    DJANGO_API_URL: str = "http://django:8000"

    REDIS_URL: str = "redis://redis:6379/0"

    LOG_LEVEL: str = "INFO"

    AI_PROVIDER: str = "mock"

    OPENROUTER_API_KEY: str = ""

    OPENROUTER_MODEL: str = (
        "deepseek/deepseek-chat-v3"
    )
    
    IMAGE_PROVIDER: str = "mock"

    FAL_API_KEY: str = ""
    
    IMAGE_MODEL: str = (
        "fal-ai/flux/schnell"
    )

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


settings = Settings()