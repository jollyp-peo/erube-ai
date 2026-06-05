from apps.characters.models import (
    CharacterVoiceAssignment,
)


def get_character_voice_assignment(
    character_id,
):
    return (
        CharacterVoiceAssignment.objects
        .select_related(
            "voice",
        )
        .filter(
            character_id=character_id,
        )
        .first()
    )