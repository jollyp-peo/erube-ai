from pydantic import BaseModel, Field

from typing import Optional


class WardrobeMemory(BaseModel):

    character_id: str

    wardrobe_id: Optional[str] = None

    outfit_name: Optional[str] = None

    accessories: list[str] = Field(
        default_factory=list
    )