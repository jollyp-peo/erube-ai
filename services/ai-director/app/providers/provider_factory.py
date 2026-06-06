import httpx

from app.core.settings import settings
from app.providers.base_ai_provider import (
    BaseAIProvider,
)


class OpenRouterProvider(
    BaseAIProvider
):

    async def generate(
        self,
        prompt: str,
    ):

        async with httpx.AsyncClient() as client:

            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization":
                        f"Bearer {settings.OPENROUTER_API_KEY}",
                    "Content-Type":
                        "application/json",
                },
                json={
                    "model":
                        settings.OPENROUTER_MODEL,
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                },
                timeout=60,
            )

            response.raise_for_status()

            return response.json()