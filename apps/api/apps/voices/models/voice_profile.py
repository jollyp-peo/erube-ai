from django.db import models

from shared.database.base_model import BaseModel


class VoiceProfile(BaseModel):

    voice = models.OneToOneField(
        "voices.Voice",
        on_delete=models.CASCADE,
        related_name="profile",
    )

    language = models.CharField(
        max_length=50,
        blank=True,
    )

    accent = models.CharField(
        max_length=100,
        blank=True,
    )

    gender = models.CharField(
        max_length=50,
        blank=True,
    )

    age_range = models.CharField(
        max_length=100,
        blank=True,
    )

    speaking_style = models.CharField(
        max_length=255,
        blank=True,
    )

    emotion_notes = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "voice_profiles"