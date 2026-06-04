from pydantic import BaseModel

from typing import List


class SceneMemory(BaseModel):

    scene_id: str

    scene_number: int

    location: str

    active_characters: List[str] = []

    summary: str