from app.writers.script_writer_factory import (
    ScriptWriterFactory,
)


class ScriptService:

    def __init__(
        self,
    ):

        self.writer = (
            ScriptWriterFactory.create()
        )

    async def generate(
        self,
        scene,
    ):

        return await self.writer.generate(
            scene
        )