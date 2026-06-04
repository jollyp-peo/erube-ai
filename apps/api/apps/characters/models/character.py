from django.db import models

from shared.database.base_model import BaseModel


class Character(BaseModel):

    STATUS_CHOICES = [
        ("active", "Active"),
        ("archived", "Archived"),
    ]

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="characters",
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_characters",
    )

    name = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        db_index=True,
    )

    description = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
    )

    class Meta:
        db_table = "characters"

    def __str__(self):
        return self.name