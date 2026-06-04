from django.db import models

from shared.database.base_model import BaseModel


class CharacterProfile(BaseModel):

    character = models.OneToOneField(
        "characters.Character",
        on_delete=models.CASCADE,
        related_name="profile",
    )

    age_range = models.CharField(
        max_length=100,
        blank=True,
    )

    gender = models.CharField(
        max_length=50,
        blank=True,
    )

    height = models.CharField(
        max_length=50,
        blank=True,
    )

    body_type = models.CharField(
        max_length=100,
        blank=True,
    )

    skin_tone = models.CharField(
        max_length=100,
        blank=True,
    )

    eye_color = models.CharField(
        max_length=100,
        blank=True,
    )

    hair_color = models.CharField(
        max_length=100,
        blank=True,
    )

    nationality = models.CharField(
        max_length=100,
        blank=True,
    )

    personality_notes = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "character_profiles"