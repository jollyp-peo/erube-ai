from django.db import models

from shared.database.base_model import BaseModel


class UserProfile(BaseModel):

    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="profile",
    )

    display_name = models.CharField(
        max_length=255,
        blank=True,
    )

    bio = models.TextField(
        blank=True,
    )

    avatar_url = models.URLField(
        blank=True,
    )
    

    website = models.URLField(
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        blank=True,
    )

    timezone = models.CharField(
        max_length=100,
        blank=True,
    )

    language = models.CharField(
        max_length=20,
        default="en",
    )

    class Meta:
        db_table = "user_profiles"