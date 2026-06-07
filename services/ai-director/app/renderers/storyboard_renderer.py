# from app.providers.mock_image_provider import (
#     MockImageProvider,
# )
from app.providers.image_provider_factory import (
    ImageProviderFactory,
)


class StoryboardRenderer:

    def __init__(
        self,
    ):
        self.provider = (
            ImageProviderFactory.create()
        )

    async def render(
        self,
        storyboard_plan,
    ):

        return (
            await self.provider.generate_image(
                prompt=(
                    storyboard_plan
                    .storyboard_prompt
                ),
                negative_prompt=(
                    storyboard_plan
                    .negative_prompt
                ),
            )
        )