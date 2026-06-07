from app.schemas.scene_script import (
    SceneScript,
)

from app.schemas.script_segment import (
    ScriptSegment,
)

from app.schemas.narration_segment import (
    NarrationSegment,
)

class MockScriptWriter:

    async def generate(
        self,
        scene,
    ):


        narration = [
            NarrationSegment(
                shot_id=scene["shots"][0]["id"],
                narration=(
                    "The market buzzed with life."
                ),
            )
        ]
        
        dialogue = [
            ScriptSegment(
                shot_id=scene["shots"][0]["id"],
                character_id="test-character",
                character_name="Prince Arin",
                dialogue=(
                    "There must be someone here "
                    "who remembers the kingdom."
                ),
                emotion="determined",
            )
        ]

        return SceneScript(
            scene_id=scene["id"],
            narration=narration,
            dialogue=dialogue,
        )