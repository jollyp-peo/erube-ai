from django.db import models

from shared.database.base_model import BaseModel


class WardrobeItem(BaseModel):

    wardrobe = models.ForeignKey(
        "wardrobes.Wardrobe",
        on_delete=models.CASCADE,
        related_name="items",
    )

    item_type = models.CharField(
        max_length=100,
    )

    color = models.CharField(
        max_length=100,
        blank=True,
    )

    material = models.CharField(
        max_length=100,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:

        db_table = "wardrobe_items"