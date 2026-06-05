from app.schemas.memory_state import MemoryState

from app.memory.scene_memory import SceneMemory
from app.memory.location_memory import LocationMemory
from app.memory.character_memory import CharacterMemory
from app.memory.voice_memory import VoiceMemory


class MemoryBuilder:

    def build(
        self,
        story,
        scenes,
        characters,
        voices,
    ) -> MemoryState:

        state = MemoryState()

        for scene in scenes:

            state.scenes.append(
                SceneMemory(
                    scene_id=scene["id"],
                    scene_number=scene["scene_number"],
                    location=scene["location"],
                    summary=scene["summary"],
                    active_characters=[
                        character["name"]
                        for character in scene.get(
                           "characters",
                            [],
                        )
                    ]
                )
            )

            state.locations.append(
                LocationMemory(
                    name=scene["location"],
                    time_of_day=scene["time_of_day"],
                )
            )

        for character in characters:

            state.characters.append(
                CharacterMemory(
                    character_id=character["id"],
                    name=character["name"],
                    voice_id=character.get(
                        "voice_id"
                    ),
                )
            )

        for voice in voices:

            state.voices.append(
                VoiceMemory(
                    voice_id=voice["id"],
                    name=voice["name"],
                )
            )

        return state