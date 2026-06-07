from abc import (
    ABC,
    abstractmethod,
)


class ImageProvider(
    ABC
):

    @abstractmethod
    async def generate_image(
        self,
        prompt: str,
        negative_prompt: str,
    ):
        pass