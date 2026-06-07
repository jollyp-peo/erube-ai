import os

import fal_client

from app.core.settings import settings

from app.schemas.generated_image import (
    GeneratedImage,
)

from app.providers.image_provider import (
    ImageProvider,
)


class FalImageProvider(
    ImageProvider
):

    async def generate_image(
        self,
        prompt: str,
        negative_prompt: str,
    ):

        os.environ[
            "FAL_KEY"
        ] = settings.FAL_API_KEY

        result = (
            await fal_client.subscribe_async(
                settings.IMAGE_MODEL,
                arguments={
                    "prompt": prompt,
                },
            )
        )

        image_url = (
            result["images"][0]["url"]
        )

        return GeneratedImage(
            image_url=image_url,
            provider="fal",
            model=settings.IMAGE_MODEL,
            prompt=prompt,
        )