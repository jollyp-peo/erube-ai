from app.core.settings import (
    settings,
)

from app.providers.mock_image_provider import (
    MockImageProvider,
)
from app.providers.fal_image_provider import (
    FalImageProvider,
)


class ImageProviderFactory:

    @staticmethod
    def create():
        provider = settings.IMAGE_PROVIDER

        if provider == "mock":
            return MockImageProvider()
        elif provider == "fal":
            return FalImageProvider()
        else:
            raise ValueError(f"Unknown image provider: {provider}")