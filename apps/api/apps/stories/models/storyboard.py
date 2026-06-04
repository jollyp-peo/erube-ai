from django.db import models

from shared.database.base_model import BaseModel


class Storyboard(BaseModel):

    scene = models.ForeignKey(
        "stories.Scene",
        on_delete=models.CASCADE,
        related_name="storyboards",
    )

    asset = models.ForeignKey(
        "assets.Asset",
        on_delete=models.CASCADE,
        related_name="storyboards",
    )

    is_primary = models.BooleanField(
        default=False,
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "storyboards"