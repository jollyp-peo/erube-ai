from app.core.settings import settings

from app.providers.mock_ai_provider import (
    MockAIProvider,
)

from app.providers.openrouter_provider import (
    OpenRouterProvider,
)


class ProviderFactory:

    @staticmethod
    def create():

        if (
            settings.AI_PROVIDER
            == "openrouter"
        ):

            return (
                OpenRouterProvider()
            )

        return MockAIProvider()