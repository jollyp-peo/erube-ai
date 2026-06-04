import logging

from app.core.settings import settings


def configure_logging():

    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),
    )

    return logging.getLogger("erube-ai-director")