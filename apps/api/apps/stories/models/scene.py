from django.db import models

from shared.database.base_model import BaseModel


class Scene(BaseModel):

    story = models.ForeignKey(
        "stories.Story",
        on_delete=models.CASCADE,
        related_name="scenes",
    )

    title = models.CharField(
        max_length=255,
    )

    scene_number = models.PositiveIntegerField()

    summary = models.TextField(
        blank=True,
    )

    location = models.CharField(
        max_length=255,
        blank=True,
    )

    time_of_day = models.CharField(
        max_length=100,
        blank=True,
    )

    duration_estimate = models.PositiveIntegerField(
        default=0,
        help_text="Estimated duration in seconds",
    )

    class Meta:
        db_table = "scenes"

        ordering = [
            "scene_number",
        ]

        unique_together = (
            "story",
            "scene_number",
        )

    def __str__(self):
        return f"{self.scene_number} - {self.title}"