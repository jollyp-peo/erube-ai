from pydantic import BaseModel


class GeneratedImage(
    BaseModel
):

    image_url: str

    provider: str

    model: str

    prompt: str