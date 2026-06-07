class StoryboardPublisher:

    def __init__(
        self,
        django_client,
    ):
        self.client = django_client

    async def publish(
        self,
        project_id,
        storyboard,
    ):

        return await self.client.create_asset(
            project_id=project_id,
            name=(
                f"Storyboard-{storyboard.shot_id}"
            ),
            asset_type="image",
            file_url=storyboard.image_url,
        )