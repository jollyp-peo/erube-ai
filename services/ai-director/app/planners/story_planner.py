from app.memory.memory_manager import MemoryManager


class StoryPlanner:

    def __init__(
        self,
        memory_manager: MemoryManager,
    ):
        self.memory_manager = memory_manager

    def create_generation_plan(
        self,
        story_id: str,
    ):

        state = self.memory_manager.get_state()

        return {
            "story_id": story_id,
            "memory_loaded": len(state.characters),
        }