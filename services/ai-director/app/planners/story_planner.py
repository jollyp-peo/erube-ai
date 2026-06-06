from app.memory.memory_manager import MemoryManager
from app.planners.scene_director import (
    SceneDirector,
)
from app.planners.shot_director import (
    ShotDirector,
)


class StoryPlanner:

    def __init__(
        self,
        memory_manager: MemoryManager,
        
    ):
        self.memory_manager = memory_manager
        self.scene_director = (
            SceneDirector()
        )
        
        self.shot_director = (
           ShotDirector()
        )

    def create_generation_plan(
        self,
        story,
        scenes,
        total_shots,
        continuity_report,
    ):

        state = self.memory_manager.get_state()
        
        scene_goals = []

        for scene in scenes:

            goal = (
                self.scene_director.build_goal(
                    scene
                )
            )

            scene_goals.append(
                {
                    "scene_id": scene["id"],
                    "scene_number": scene[
                        "scene_number"
                    ],
                    "title": scene["title"],
                    "goal": goal.model_dump(),
                }
            )
            
        shot_goals = []

        for scene in scenes:
        
            for shot in scene["shots"]:
        
                goal = (
                    self.shot_director.build_goal(
                        shot
                    )
                )
        
                shot_goals.append(
                    {
                        "scene_id": scene["id"],
                        "shot_id": shot["id"],
                        "shot_number": shot[
                            "shot_number"
                        ],
                        "title": shot["title"],
                        "goal": goal.model_dump(),
                    }
                )
        
        return {
            "story_id": story["id"],
            "title": story["title"],
            "genre": story["genre"],
            "total_scenes": len(scenes),
            "total_shots": total_shots,
            "continuity": continuity_report,
            "scene_goals": scene_goals,
            "shot_goals": shot_goals,
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