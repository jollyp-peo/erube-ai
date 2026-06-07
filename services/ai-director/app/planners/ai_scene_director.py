import json

from app.schemas.scene_goal import (
    SceneGoal,
)

from app.providers.retry_handler import (
    RetryHandler,
)

from app.providers.ai_json_validator import (
    AIJSONValidator,
)

from app.providers.ai_response_handler import (
    AIResponseHandler,
)


class AISceneDirector:

    def __init__(
        self,
        provider,
    ):
        self.provider = provider

    async def build_goal(
        self,
        story,
        scene,
    ):

        prompt = f"""
        Story:
        {story["title"]}

        Scene:
        {scene["summary"]}

        Return ONLY valid JSON.

        {{
            "objective": "",
            "emotional_tone": "",
            "visual_style": ""
        }}
        """

        response = (
            await RetryHandler.execute(
                lambda: self.provider.generate(
                    prompt
                )
            )
        )

        data = (
            AIResponseHandler.parse(
                response,
                AIJSONValidator.validate_scene_goal,
            )
        )
        
        return SceneGoal(
            objective=data[
                "objective"
            ],
            emotional_tone=data[
                "emotional_tone"
            ],
            visual_style=data[
                "visual_style"
            ],
        )