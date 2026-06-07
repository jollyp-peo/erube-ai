from pydantic import BaseModel


class NarrationSegment(
    BaseModel
):

    shot_id: str

    narration: str