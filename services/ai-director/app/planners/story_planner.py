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

        state = self.memory_manager.get_state()

        return {
            "story_id": story["id"],
            "title": story["title"],
            "genre": story["genre"],
            "total_scenes": len(scenes),
            "total_shots": total_shots,
            "memory": {
                "scenes": [
                    {
                        "scene_id": scene.scene_id,
                        "scene_number": scene.scene_number,
                        "location": scene.location,
                    }
                    for scene in state.scenes
                ],
                "locations": [
                    {
                        "name": location.name,
                        "time_of_day": location.time_of_day,
                    }
                    for location in state.locations
                ],
                "characters": [
                    {
                        "character_id": character.character_id,
                        "name": character.name,
                    }
                    for character in state.characters
                ],
                "voices": [
                    {
                        "voice_id": voice.voice_id,
                        "name": voice.name,
                    }
                    for voice in state.voices
                ],
            },
            "scenes": scenes,
        }