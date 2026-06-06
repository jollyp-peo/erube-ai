from app.schemas.shot_goal import (
    ShotGoal,
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

        Generate:
        purpose,
        framing_intent,
        narrative_intent
        """

        result = (
            await self.provider.generate(
                prompt
            )
        )

        return ShotGoal(
            purpose=result[
                "purpose"
            ],
            framing_intent=result[
                "framing_intent"
            ],
            narrative_intent=result[
                "narrative_intent"
            ],
        )