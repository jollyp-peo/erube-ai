from typing import List, Optional

from pydantic import BaseModel, Field
from app.schemas.shot_goal import ShotGoal
from app.schemas.prompt_package import (
    PromptPackage,
)

from app.schemas.storyboard_plan import (
    StoryboardPlan,
)


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

    goal: Optional[ShotGoal] = None
    
    storyboard_plan: (
        StoryboardPlan | None
    ) = None

    prompt_package: Optional[
        PromptPackage
    ] = None
    
    
    characters: List[CharacterContext] = Field(
        default_factory=list
    )

    voice: Optional[VoiceContext] = None

    location: Optional[LocationContext] = None

    storyboards: List[StoryboardContext] = Field(
        default_factory=list
    )