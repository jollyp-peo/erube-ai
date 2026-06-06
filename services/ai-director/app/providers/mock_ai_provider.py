from app.providers.base_ai_provider import (
    BaseAIProvider,
)


class MockAIProvider(
    BaseAIProvider
):

    async def generate(
        self,
        prompt: str,
    ):

        if "purpose" in prompt:

            return {
                "purpose": (
                    "Introduce environment"
                ),
                "framing_intent": (
                    "Show scale and setting"
                ),
                "narrative_intent": (
                    "Orient audience"
                ),
            }

        return {
            "objective": (
                "Search for information"
            ),
            "emotional_tone": (
                "curious"
            ),
            "visual_style": (
                "fantasy adventure"
            ),
        }