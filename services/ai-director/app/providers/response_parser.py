class ResponseParser:

    @staticmethod
    def extract_content(
        response,
    ):

        content = (
            response["choices"][0]
            ["message"]
            ["content"]
        )

        content = content.strip()

        if content.startswith(
            "```json"
        ):

            content = content.replace(
                "```json",
                "",
                1,
            )

        if content.endswith(
            "```"
        ):

            content = content[:-3]

        return content.strip()