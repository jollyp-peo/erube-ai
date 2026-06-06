from pydantic import BaseModel


class ShotGoal(BaseModel):

    purpose: str

    framing_intent: str

    narrative_intent: str