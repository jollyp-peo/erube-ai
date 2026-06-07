from app.memory.memory_manager import MemoryManager

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
# Real data openrouter
from app.planners.ai_scene_director import (
    AISceneDirector,
)

from app.planners.ai_shot_director import (
    AIShotDirector,
)

from app.providers.provider_factory import (
    ProviderFactory,
)

from app.planners.storyboard_director import (
    StoryboardDirector,
)

from app.planners.storyboard_prompt_builder import (
    StoryboardPromptBuilder,
)

from app.writers.script_service import (
    ScriptService,
)

from app.renderers.storyboard_service import (
    StoryboardService,
)

from app.schemas.shot_plan import (
    StoryboardContext,
)

class StoryPlanner:

    def __init__(
        self,
        memory_manager: MemoryManager,
        
    ):
        self.memory_manager = memory_manager
        
        provider = (
           ProviderFactory.create()
        )

        self.scene_director = (
            AISceneDirector(
                provider
            )
        )
        
        self.shot_director = (
            AIShotDirector(
                provider
            )
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
        
        self.storyboard_prompt_builder = (
            StoryboardPromptBuilder()
        )
    
        self.storyboard_director = (
            StoryboardDirector()
        )
        
        
        self.script_service = (
            ScriptService()
        )
        
        self.storyboard_service = (
            StoryboardService()
        )

    async def create_generation_plan(
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
                await self.scene_director.build_goal(
                    story,
                    scene,
                )
            )
            
            scene_script = (
                await self.script_service.generate(
                    scene
                )
            )
            
            
            shot_plans = []
        
            for shot in scene["shots"]:
        
                shot_goal = (
                    await self.shot_director.build_goal(
                        scene,
                        shot,
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
                
                storyboard_prompt = (
                    self.storyboard_prompt_builder.build(
                        shot_plan
                    )
                )

                storyboard_plan = (
                    self.storyboard_director.build(
                        shot_plan,
                        storyboard_prompt,
                    )
                )
                shot_plan.storyboard_plan = (
                    storyboard_plan
                )
                
                if shot_plan.storyboard_plan:

                    storyboard_result = (
                        await self.storyboard_service.generate(
                            project_id=story[
                                "project_id"
                            ],
                            storyboard_plan=(
                                shot_plan.storyboard_plan
                            ),
                        )
                    )
                
                    shot_plan.storyboards.append(
                        StoryboardContext(
                            asset_id=(
                                storyboard_result[
                                    "asset"
                                ][
                                    "asset_id"
                                ]
                            ),
                            is_primary=True,
                        )
                    )
        
                shot_plans.append(
                    shot_plan
                )

            scene_plan = (
                self.plan_builder.build_scene_plan(
                    scene=scene,
                    goal=scene_goal,
                    script=scene_script,
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