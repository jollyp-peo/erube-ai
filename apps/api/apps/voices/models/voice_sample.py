from django.db import models

from shared.database.base_model import BaseModel


class VoiceSample(BaseModel):

    SAMPLE_TYPES = [
        ("training", "Training"),
        ("reference", "Reference"),
        ("emotion", "Emotion"),
        ("conversation", "Conversation"),
        ("narration", "Narration"),
    ]

    voice = models.ForeignKey(
        "voices.Voice",
        on_delete=models.CASCADE,
        related_name="samples",
    )

    asset = models.ForeignKey(
        "assets.Asset",
        on_delete=models.CASCADE,
        related_name="voice_samples",
    )

    sample_type = models.CharField(
        max_length=50,
        choices=SAMPLE_TYPES,
    )

    weight = models.FloatField(
        default=1.0,
    )

    is_primary = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "voice_samples"