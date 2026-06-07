import json

from app.schemas.shot_goal import (
    ShotGoal,
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


class AIShotDirector:

    def __init__(
        self,
        provider,
    ):
        self.provider = provider

    async def build_goal(
        self,
        scene,
        shot,
    ):

        prompt = f"""
        Scene:
        {scene["summary"]}

        Shot:
        {shot["title"]}

        Description:
        {shot["description"]}

        Return ONLY valid JSON.

        {{
            "purpose": "",
            "framing_intent": "",
            "narrative_intent": ""
        }}
        """

        response = await RetryHandler.execute(
            lambda: self.provider.generate(
                prompt
            )
        )

        data = (
            AIResponseHandler.parse(
                response,
                AIJSONValidator.validate_shot_goal,
            )
        )
        
        return ShotGoal(
            purpose=data[
                "purpose"
            ],
            framing_intent=data[
                "framing_intent"
            ],
            narrative_intent=data[
                "narrative_intent"
            ],
        )