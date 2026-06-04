from django.db import models

from shared.database.base_model import BaseModel


class Organization(BaseModel):

    name = models.CharField(
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
        db_index=True,
    )

    owner = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="owned_organizations",
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "organizations"

    def __str__(self):
        return self.name