from app.renderers.storyboard_renderer import (
    StoryboardRenderer,
)

from app.renderers.storyboard_asset_builder import (
    StoryboardAssetBuilder,
)

from app.renderers.storyboard_publisher import (
    StoryboardPublisher,
)

from app.clients.django_client import (
    DjangoClient,
)


class StoryboardService:

    def __init__(self):

        self.renderer = (
            StoryboardRenderer()
        )

        self.asset_builder = (
            StoryboardAssetBuilder()
        )

        self.publisher = (
            StoryboardPublisher(
                DjangoClient()
            )
        )

    async def generate(
        self,
        project_id,
        storyboard_plan,
    ):

        image = (
            await self.renderer.render(
                storyboard_plan
            )
        )

        storyboard = (
            self.asset_builder.build(
                shot_id=(
                    storyboard_plan.shot_id
                ),
                image=image,
            )
        )

        asset = (
            await self.publisher.publish(
                project_id=project_id,
                storyboard=storyboard,
            )
        )

        return {
            "storyboard": (
                storyboard.model_dump()
            ),
            "asset": asset,
        }