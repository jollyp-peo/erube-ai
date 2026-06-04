from django.db import models

from shared.database.base_model import BaseModel


class Project(BaseModel):

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="projects",
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_projects",
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

    is_archived = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.name