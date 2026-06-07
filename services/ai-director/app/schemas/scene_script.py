from pydantic import BaseModel

from app.schemas.narration_segment import (
    NarrationSegment,
)

from app.schemas.script_segment import (
    ScriptSegment,
)


class SceneScript(
    BaseModel
):

    scene_id: str

    narration: list[
        NarrationSegment
    ]

    dialogue: list[
        ScriptSegment
    ]