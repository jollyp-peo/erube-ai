import asyncio


class RetryHandler:

    @staticmethod
    async def execute(
        operation,
        retries=3,
        delay=1,
    ):

        last_error = None

        for attempt in range(
            retries
        ):

            try:

                return await operation()

            except Exception as e:

                last_error = e

                if (
                    attempt < retries - 1
                ):

                    await asyncio.sleep(
                        delay
                    )

        raise last_error