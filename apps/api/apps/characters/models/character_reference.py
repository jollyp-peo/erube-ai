from django.db import models

from shared.database.base_model import BaseModel


class CharacterReference(BaseModel):

    REFERENCE_TYPES = [
        ("face", "Face"),
        ("body", "Body"),
        ("full_body", "Full Body"),
        ("clothing", "Clothing"),
        ("expression", "Expression"),
        ("pose", "Pose"),
    ]

    character = models.ForeignKey(
        "characters.Character",
        on_delete=models.CASCADE,
        related_name="references",
    )

    asset = models.ForeignKey(
        "assets.Asset",
        on_delete=models.CASCADE,
        related_name="character_references",
    )

    reference_type = models.CharField(
        max_length=50,
        choices=REFERENCE_TYPES,
    )

    weight = models.FloatField(
        default=1.0,
    )

    is_primary = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "character_references"