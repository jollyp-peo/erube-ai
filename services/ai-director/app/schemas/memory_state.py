from typing import List

from pydantic import BaseModel, Field
from app.memory.character_memory import CharacterMemory
from app.memory.voice_memory import VoiceMemory
from app.memory.scene_memory import SceneMemory
from app.memory.location_memory import LocationMemory
from app.memory.wardrobe_memory import WardrobeMemory



class MemoryState(BaseModel):

    characters: List[CharacterMemory] = Field(
        default_factory=list
    )

    voices: List[VoiceMemory] = Field(
        default_factory=list
    )

    scenes: List[SceneMemory] = Field(
        default_factory=list
    )

    locations: List[LocationMemory] = Field(
        default_factory=list
    )

    wardrobes: List[WardrobeMemory] = Field(
        default_factory=list
    )