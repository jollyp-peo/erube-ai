from django.db import models

from shared.database.base_model import BaseModel


class CharacterVoiceAssignment(BaseModel):

    character = models.OneToOneField(
        "characters.Character",
        on_delete=models.CASCADE,
        related_name="voice_assignment",
    )

    voice = models.ForeignKey(
        "voices.Voice",
        on_delete=models.CASCADE,
        related_name="assigned_characters",
    )

    is_primary = models.BooleanField(
        default=True,
    )

    class Meta:

        db_table = "character_voice_assignments"