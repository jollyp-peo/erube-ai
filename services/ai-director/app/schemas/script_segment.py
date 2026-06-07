from pydantic import BaseModel


class ScriptSegment(
    BaseModel
):

    shot_id: str

    character_id: str

    character_name: str

    dialogue: str

    emotion: str