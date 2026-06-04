from typing import List, Optional

from pydantic import BaseModel, Field


class CharacterContext(BaseModel):
    character_id: str
    name: str
    wardrobe: Optional[str] = None


class VoiceContext(BaseModel):
    voice_id: str
    name: str
    language: Optional[str] = None
    accent: Optional[str] = None


class LocationContext(BaseModel):
    name: str
    time_of_day: Optional[str] = None


class StoryboardContext(BaseModel):
    asset_id: str
    is_primary: bool = False


class ShotPlan(BaseModel):

    shot_id: str

    scene_number: int

    shot_number: int

    title: str

    description: Optional[str] = None

    camera_type: Optional[str] = None

    camera_movement: Optional[str] = None

    duration_seconds: int = Field(
        default=5,
        ge=1,
    )

    prompt: str

    negative_prompt: Optional[str] = None

    characters: List[CharacterContext] = []

    voice: Optional[VoiceContext] = None

    location: Optional[LocationContext] = None

    storyboards: List[StoryboardContext] = []