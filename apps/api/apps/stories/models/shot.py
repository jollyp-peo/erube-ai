from django.db import models

from shared.database.base_model import BaseModel


class Shot(BaseModel):

    scene = models.ForeignKey(
        "stories.Scene",
        on_delete=models.CASCADE,
        related_name="shots",
    )

    shot_number = models.PositiveIntegerField()

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
    )

    camera_type = models.CharField(
        max_length=100,
        blank=True,
    )

    camera_movement = models.CharField(
        max_length=100,
        blank=True,
    )

    duration_seconds = models.PositiveIntegerField(
        default=5,
    )

    class Meta:
        db_table = "shots"

        ordering = [
            "shot_number",
        ]

        unique_together = (
            "scene",
            "shot_number",
        )

    def __str__(self):
        return f"{self.shot_number} - {self.title}"