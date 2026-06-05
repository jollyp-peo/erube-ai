from app.memory.memory_manager import MemoryManager


class StoryPlanner:

    def __init__(
        self,
        memory_manager: MemoryManager,
    ):
        self.memory_manager = memory_manager

    def create_generation_plan(
        self,
        story,
        scenes,
        total_shots,
    ):

        return {
            "story_id": story["id"],
            "title": story["title"],
            "total_scenes": len(scenes),
            "total_shots": total_shots,
            "scenes": scenes,
        }