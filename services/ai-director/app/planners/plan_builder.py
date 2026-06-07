from app.schemas.scene_plan import ScenePlan
from app.schemas.shot_plan import ShotPlan


class PlanBuilder:

    def build_shot_plan(
        self,
        shot,
        goal,
        scene_number,
    ):

        return ShotPlan(
            shot_id=shot["id"],
            scene_number=scene_number,
            shot_number=shot["shot_number"],
            title=shot["title"],
            description=shot.get(
                "description"
            ),
            camera_type=shot.get(
                "camera_type"
            ),
            camera_movement=shot.get(
                "camera_movement"
            ),
            duration_seconds=shot.get(
                "duration_seconds",
                5,
            ),
            goal=goal,
            prompt="",
        )

    def build_scene_plan(
        self,
        scene,
        goal,
        script,
        shot_plans,
    ):

        return ScenePlan(
            scene_id=scene["id"],
            scene_number=scene[
                "scene_number"
            ],
            title=scene["title"],
            location=scene["location"],
            time_of_day=scene[
                "time_of_day"
            ],
            estimated_duration=scene[
                "duration_estimate"
            ],
            goal=goal,
            script=script,
            shots=shot_plans,
        )