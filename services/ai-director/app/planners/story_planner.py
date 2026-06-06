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
        continuity_report,
    ):

        state = self.memory_manager.get_state()

        return {
            "story_id": story["id"],
            "title": story["title"],
            "genre": story["genre"],
            "total_scenes": len(scenes),
            "total_shots": total_shots,
            "continuity": continuity_report,
            "memory": {
                "scenes": [
                    {
                        "scene_id": scene.scene_id,
                        "scene_number": scene.scene_number,
                        "location": scene.location,
                        "active_characters": (
                            scene.active_characters
                        ),
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
                        "voice_id": character.voice_id,
                        "personality": character.personality,
                        "gender": character.gender,
                        "hair_color": character.hair_color,
                        "eye_color": character.eye_color,
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
                "wardrobes": [
                    {
                        "character_id": wardrobe.character_id,
                        "wardrobe_id": wardrobe.wardrobe_id,
                        "outfit_name": wardrobe.outfit_name,
                    }
                    for wardrobe in state.wardrobes
                ],
                
            },
            "scenes": scenes,
        }