from apps.characters.models import CharacterProfile


def get_character_profile(
    character_id,
):
    return (
        CharacterProfile.objects
        .filter(
            character_id=character_id,
        )
        .first()
    )