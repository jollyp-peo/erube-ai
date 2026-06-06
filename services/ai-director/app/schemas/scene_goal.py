from pydantic import BaseModel


class SceneGoal(BaseModel):

    objective: str

    emotional_tone: str

    visual_style: str