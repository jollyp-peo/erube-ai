import json


from app.providers.ai_json_validator import (
    AIJSONValidator,
)

from app.schemas.scene_script import (
    SceneScript,
)

from app.schemas.script_segment import (
    ScriptSegment,
)

from app.schemas.narration_segment import (
    NarrationSegment,
)

from app.providers.ai_response_handler import (
    AIResponseHandler,
)

class AIScriptWriter:

    def __init__(
        self,
        provider,
    ):
        self.provider = provider
        
    async def generate(
        self,
        scene,
    ):
        
        characters_text = ""

        for character in scene[
            "characters"
        ]:
        
            characters_text += f"""
            Character ID:
            {character["character_id"]}
        
            Name:
            {character["name"]}
        
            Speaking:
            {character["is_speaking"]}
            """
            
        shots_text = ""

        for shot in scene[
            "shots"
        ]:
        
            shots_text += f"""
            Shot ID:
            {shot["id"]}
        
            Title:
            {shot["title"]}
        
            Description:
            {shot["description"]}
            """
            
        prompt = f"""
        Scene Title:
            {scene["title"]}
        
        Scene Summary:
            {scene["summary"]}
        
        Location:
            {scene["location"]}
        
        Time Of Day:
            {scene["time_of_day"]}
        
        Characters:
            {characters_text}
        
        Shots:
            {shots_text}
        
            Generate narration
            for each shot.
            
            Generate dialogue
            only for characters
            where Speaking=True.
            
            Return ONLY valid JSON.
        
        {{
            "narration": [
                {{
                    "shot_id": "",
                    "narration": ""
                }}
            ],
            "dialogue": [
                {{
                    "shot_id": "",
                    "character_id": "",
                    "character_name": "",
                    "dialogue": "",
                    "emotion": ""
                }}
            ]
        }}
        """
        
        response = (
            await self.provider.generate(
                prompt
            )
        )

        data = (
            AIResponseHandler.parse(
                response,
                AIJSONValidator.validate_scene_script,
            )
        )
        
        
        narration_segments = []

        for item in data[
            "narration"
        ]:
        
            narration_segments.append(
                NarrationSegment(
                    shot_id=item[
                        "shot_id"
                    ],
                    narration=item[
                        "narration"
                    ],
                )
            )
            
        dialogue_segments = []

        for item in data[
            "dialogue"
        ]:
        
            dialogue_segments.append(
                ScriptSegment(
                    shot_id=item[
                        "shot_id"
                    ],
                    character_id=item[
                        "character_id"
                    ],
                    character_name=item[
                        "character_name"
                    ],
                    dialogue=item[
                        "dialogue"
                    ],
                    emotion=item[
                        "emotion"
                    ],
                )
            )
            
        return SceneScript(
            scene_id=scene["id"],
            narration=narration_segments,
            dialogue=dialogue_segments,
        )