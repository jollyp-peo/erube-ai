from django.db import models

from shared.database.base_model import BaseModel


class Asset(BaseModel):

    ASSET_TYPES = [
        ("image", "Image"),
        ("video", "Video"),
        ("audio", "Audio"),
        ("document", "Document"),
        ("model", "Model"),
        ("other", "Other"),
    ]

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="assets",
    )

    uploaded_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="uploaded_assets",
    )

    name = models.CharField(
        max_length=255,
    )

    asset_type = models.CharField(
        max_length=50,
        choices=ASSET_TYPES,
    )

    file_url = models.TextField()

    file_size = models.BigIntegerField(
        default=0,
    )

    mime_type = models.CharField(
        max_length=255,
        blank=True,
    )

    class Meta:
        db_table = "assets"

    def __str__(self):
        return self.name