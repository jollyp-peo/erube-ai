from app.memory.memory_manager import MemoryManager


class ScenePlanner:

    def __init__(
        self,
        memory_manager: MemoryManager,
    ):
        self.memory_manager = memory_manager

    def plan_scene(
        self,
        scene_id: str,
    ):

        return {
            "scene_id": scene_id,
        }