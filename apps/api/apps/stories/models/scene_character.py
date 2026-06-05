from django.db import models

from shared.database.base_model import BaseModel


class SceneCharacter(BaseModel):

    scene = models.ForeignKey(
        "stories.Scene",
        on_delete=models.CASCADE,
        related_name="scene_characters",
    )

    character = models.ForeignKey(
        "characters.Character",
        on_delete=models.CASCADE,
        related_name="character_scenes",
    )

    role_name = models.CharField(
        max_length=100,
        blank=True,
    )

    is_speaking = models.BooleanField(
        default=False,
    )

    importance = models.PositiveSmallIntegerField(
        default=1,
    )

    class Meta:

        db_table = "scene_characters"

        unique_together = (
            "scene",
            "character",
        )