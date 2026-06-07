from app.schemas.generated_storyboard import (
    GeneratedStoryboard,
)


class StoryboardAssetBuilder:

    def build(
        self,
        shot_id,
        image,
    ):

        return GeneratedStoryboard(
            shot_id=shot_id,
            image_url=image.image_url,
            provider=image.provider,
            model=image.model,
            prompt=image.prompt,
        )