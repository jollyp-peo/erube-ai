from pydantic import BaseModel

from typing import Optional


class CharacterMemory(BaseModel):

    character_id: str

    name: str

    voice_id: Optional[str] = None

    personality: Optional[str] = None

    wardrobe: Optional[str] = None