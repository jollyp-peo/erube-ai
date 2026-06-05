from django.db import models

from shared.database.base_model import BaseModel


class Wardrobe(BaseModel):

    character = models.ForeignKey(
        "characters.Character",
        on_delete=models.CASCADE,
        related_name="wardrobes",
    )

    name = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
    )

    is_default = models.BooleanField(
        default=False,
    )

    class Meta:

        db_table = "wardrobes"