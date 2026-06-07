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
                f"{self.base_url}/internal/stories/{story_id}/"
            )

            response.raise_for_status()

            return response.json()


    async def get_story_scenes(
        self,
        story_id: str,
    ):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/internal/stories/{story_id}/scenes/"
            )

            response.raise_for_status()

            return response.json()


    async def get_scene_shots(
        self,
        scene_id: str,
    ):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/internal/scenes/{scene_id}/shots/"
            )

            response.raise_for_status()

            return response.json()
        
        
        
    async def get_project_characters(
        self,
        project_id: str,
    ):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/internal/projects/{project_id}/characters/"
            )

            response.raise_for_status()

            return response.json()


    async def get_project_voices(
        self,
        project_id: str,
    ):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/internal/projects/{project_id}/voices/"
            )

            response.raise_for_status()

            return response.json()
    
    async def get_scene_characters(
        self,
        scene_id: str,
    ):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/internal/scenes/{scene_id}/characters/"
            )

            response.raise_for_status()

        return response.json()
    
    
    async def get_character_voice(
        self,
        character_id: str,
    ):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/internal/characters/{character_id}/voice/"
            )

            response.raise_for_status()

        return response.json()
    
    
    async def get_character_profile(
        self,
        character_id: str,
    ):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/internal/characters/{character_id}/profile/"
            )

            response.raise_for_status()

        return response.json()
    
    async def get_scene_wardrobes(
        self,
        scene_id: str,
    ):
        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{self.base_url}/internal/scenes/{scene_id}/wardrobes/"
        )

        response.raise_for_status()

        return response.json()
    
    # Assets storage
    
    async def create_asset(
        self,
        project_id,
        name,
        asset_type,
        file_url,
    ):

        async with httpx.AsyncClient() as client:
    
            response = await client.post(
                f"{self.base_url}/internal/assets/",
                json={
                    "project_id": project_id,
                    "name": name,
                    "asset_type": asset_type,
                    "file_url": file_url,
                },
            )
    
            response.raise_for_status()
    
            return response.json()