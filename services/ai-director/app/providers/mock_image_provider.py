from app.schemas.generated_image import (
    GeneratedImage,
)

from app.providers.image_provider import (
    ImageProvider,
)


class MockImageProvider(
    ImageProvider
):

    async def generate_image(
        self,
        prompt: str,
        negative_prompt: str,
    ):

        return GeneratedImage(
            image_url=(
                "https://example.com/storyboard.jpg"
            ),
            provider="mock",
            model="mock-image-model",
            prompt=prompt,
        )