from app.schemas.memory_state import MemoryState

from app.memory.scene_memory import SceneMemory
from app.memory.location_memory import LocationMemory


class MemoryBuilder:

    def build(
        self,
        story,
        scenes,
    ) -> MemoryState:

        state = MemoryState()

        for scene in scenes:

            state.scenes.append(
                SceneMemory(
                    scene_id=scene["id"],
                    scene_number=scene["scene_number"],
                    location=scene["location"],
                    summary=scene["summary"],
                    active_characters=[],
                )
            )

            state.locations.append(
                LocationMemory(
                    name=scene["location"],
                    time_of_day=scene["time_of_day"],
                )
            )

        return state