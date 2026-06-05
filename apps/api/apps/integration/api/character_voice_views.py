from django.http import JsonResponse

from apps.integration.selectors.character_voice_selector import (
    get_character_voice_assignment,
)


def internal_character_voice(
    request,
    character_id,
):
    assignment = (
        get_character_voice_assignment(
            character_id=character_id,
        )
    )

    if not assignment:

        return JsonResponse(
            {
                "voice": None,
            }
        )

    return JsonResponse(
        {
            "voice": {
                "voice_id": str(
                    assignment.voice.id
                ),
                "name": assignment.voice.name,
                "is_primary": assignment.is_primary,
            }
        }
    )