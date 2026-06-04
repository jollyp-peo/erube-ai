from typing import List

from pydantic import BaseModel

from app.schemas.shot_plan import ShotPlan


class ScenePlan(BaseModel):

    scene_id: str

    scene_number: int

    title: str

    location: str

    time_of_day: str

    estimated_duration: int

    shots: List[ShotPlan]