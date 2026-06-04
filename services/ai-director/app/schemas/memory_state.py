from typing import List

from pydantic import BaseModel

from app.memory.character_memory import CharacterMemory
from app.memory.voice_memory import VoiceMemory
from app.memory.scene_memory import SceneMemory
from app.memory.location_memory import LocationMemory
from app.memory.wardrobe_memory import WardrobeMemory


class MemoryState(BaseModel):

    characters: List[CharacterMemory] = []

    voices: List[VoiceMemory] = []

    scenes: List[SceneMemory] = []

    locations: List[LocationMemory] = []

    wardrobes: List[WardrobeMemory] = []