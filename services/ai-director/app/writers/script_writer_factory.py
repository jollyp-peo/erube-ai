from app.providers.provider_factory import (
    ProviderFactory,
)

from app.writers.ai_script_writer import (
    AIScriptWriter,
)


class ScriptWriterFactory:

    @staticmethod
    def create():

        provider = (
            ProviderFactory.create()
        )

        return AIScriptWriter(
            provider
        )