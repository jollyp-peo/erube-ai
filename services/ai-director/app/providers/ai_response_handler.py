import json

from app.providers.response_parser import (
    ResponseParser,
)


class AIResponseHandler:

    @staticmethod
    def parse(
        response,
        validator,
    ):

        content = (
            ResponseParser.extract_content(
                response
            )
        )

        data = json.loads(
            content
        )

        validator(
            data
        )

        return data