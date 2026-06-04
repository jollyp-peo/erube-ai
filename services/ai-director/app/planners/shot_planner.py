from app.memory.memory_manager import MemoryManager


class ShotPlanner:

    def __init__(
        self,
        memory_manager: MemoryManager,
    ):
        self.memory_manager = memory_manager

    def plan_shot(
        self,
        shot_id: str,
    ):

        state = self.memory_manager.get_state()

        return {
            "shot_id": shot_id,
            "characters": len(state.characters),
            "voices": len(state.voices),
        }