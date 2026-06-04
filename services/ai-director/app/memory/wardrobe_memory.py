from pydantic import BaseModel

from typing import Optional


class WardrobeMemory(BaseModel):

    character_id: str

    outfit_name: Optional[str] = None

    accessories: list[str] = []