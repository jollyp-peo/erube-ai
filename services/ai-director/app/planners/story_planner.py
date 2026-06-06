from app.memory.memory_manager import MemoryManager
from app.planners.scene_director import (
    SceneDirector,
)
from app.planners.shot_director import (
    ShotDirector,
)

from app.planners.plan_builder import (
    PlanBuilder,
)

from app.planners.context_builder import (
    ContextBuilder,
)

from app.planners.cinematic_prompt_builder import (
    CinematicPromptBuilder,
)

from app.planners.prompt_package_builder import (
    PromptPackageBuilder
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
        
        self.plan_builder = (
            PlanBuilder()
        )
        
        self.context_builder = (
           ContextBuilder()
        )
        
        self.prompt_builder = (
            CinematicPromptBuilder()
        )
        
        self.prompt_package_builder = (
            PromptPackageBuilder()
        )


    def create_generation_plan(
        self,
        story,
        scenes,
        total_shots,
        continuity_report,
    ):

        state = self.memory_manager.get_state()
        
        scene_plans = []
        
        for scene in scenes:

            scene_goal = (
                self.scene_director.build_goal(
                    scene
                )
            )

            shot_plans = []
        
            for shot in scene["shots"]:
        
                shot_goal = (
                    self.shot_director.build_goal(
                        shot
                    )
                )
        
                shot_plan = (
                    self.plan_builder.build_shot_plan(
                        shot=shot,
                        scene_number=scene[
                            "scene_number"
                        ],
                        goal=shot_goal,
                    )
                )
                shot_plan.characters = (
                    self.context_builder
                        .build_character_contexts(
                            scene,
                            state,
                        )
                    )

                shot_plan.location = (
                    self.context_builder
                    .build_location_context(
                        scene
                    )
                )
                
                shot_plan.voice = (
                    self.context_builder
                    .build_voice_context(
                        scene,
                        state,
                    )
                )
                prompt = (
                    self.prompt_builder.build(
                        shot_plan
                    )
                )

                shot_plan.prompt_package = (
                    self.prompt_package_builder.build(
                        shot_plan,
                        prompt,
                    )
                )
                
        
                shot_plans.append(
                    shot_plan
                )

            scene_plan = (
                self.plan_builder.build_scene_plan(
                    scene=scene,
                    goal=scene_goal,
                    shot_plans=shot_plans,
                )
            )
        
            scene_plans.append(
                scene_plan
            )
                
                
        return {
            "story_id": story["id"],
            "title": story["title"],
            "genre": story["genre"],
            "total_scenes": len(scenes),
            "total_shots": total_shots,
            "continuity": continuity_report,
            "scene_plans": [
                plan.model_dump()
                for plan in scene_plans
            ],
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