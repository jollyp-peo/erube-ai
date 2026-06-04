from typing import List

from pydantic import BaseModel

from app.schemas.scene_plan import ScenePlan


class GenerationPlan(BaseModel):

    generation_id: str

    project_id: str

    story_id: str

    total_scenes: int

    total_shots: int

    estimated_duration: int

    scenes: List[ScenePlan]