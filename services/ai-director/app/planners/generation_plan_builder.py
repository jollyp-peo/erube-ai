from app.schemas.generation_plan import (
    GenerationPlan,
)


class GenerationPlanBuilder:

    def build(
        self,
        story,
        scenes,
        total_shots,
    ):

        return GenerationPlan(
            generation_id="temp",
            project_id="temp",
            story_id=story["id"],
            total_scenes=len(scenes),
            total_shots=total_shots,
            estimated_duration=sum(
                shot["duration_seconds"]
                for scene in scenes
                for shot in scene["shots"]
            ),
            scenes=[],
        )