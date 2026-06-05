from pydantic import BaseModel

from typing import Optional


class CharacterMemory(BaseModel):

    character_id: str

    name: str

    voice_id: Optional[str] = None

    personality: Optional[str] = None

    wardrobe: Optional[str] = None

    age_range: Optional[str] = None

    gender: Optional[str] = None

    height: Optional[str] = None

    body_type: Optional[str] = None

    skin_tone: Optional[str] = None

    eye_color: Optional[str] = None

    hair_color: Optional[str] = None

    nationality: Optional[str] = None