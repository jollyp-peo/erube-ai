from typing import List

from pydantic import BaseModel, Field


class PromptPackage(BaseModel):

    prompt: str

    negative_prompt: str = ""

    style_tags: List[str] = Field(
        default_factory=list
    )

    camera_tags: List[str] = Field(
        default_factory=list
    )

    lighting_tags: List[str] = Field(
        default_factory=list
    )