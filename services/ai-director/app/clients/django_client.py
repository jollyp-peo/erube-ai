import httpx

from app.core.settings import settings


class DjangoClient:

    def __init__(self):
        self.base_url = settings.DJANGO_API_URL

    async def get_story(
        self,
        story_id: str,
    ):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/api/v1/stories/{story_id}/"
            )

            response.raise_for_status()

            return response.json()

    async def get_characters(
        self,
        story_id: str,
    ):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/api/v1/stories/{story_id}/characters/"
            )

            response.raise_for_status()

            return response.json()

    async def get_scenes(
        self,
        story_id: str,
    ):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/api/v1/stories/{story_id}/scenes/"
            )

            response.raise_for_status()

            return response.json()