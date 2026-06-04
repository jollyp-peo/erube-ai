from django.db import models

from shared.database.base_model import BaseModel


class Story(BaseModel):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("in_review", "In Review"),
        ("approved", "Approved"),
        ("archived", "Archived"),
    ]

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="stories",
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_stories",
    )

    title = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        db_index=True,
    )

    description = models.TextField(
        blank=True,
    )

    genre = models.CharField(
        max_length=100,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )

    class Meta:
        db_table = "stories"

    def __str__(self):
        return self.title