from pydantic import BaseModel


class GeneratedStoryboard(
    BaseModel
):

    shot_id: str

    image_url: str

    provider: str

    model: str

    prompt: str