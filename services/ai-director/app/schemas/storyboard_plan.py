from pydantic import BaseModel


class StoryboardPlan(BaseModel):

    shot_id: str

    storyboard_prompt: str

    negative_prompt: str

    aspect_ratio: str = "16:9"

    style: str = "cinematic"

    image_count: int = 1