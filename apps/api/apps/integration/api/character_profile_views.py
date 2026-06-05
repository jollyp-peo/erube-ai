from django.http import JsonResponse

from apps.integration.selectors.character_profile_selector import (
    get_character_profile,
)


def internal_character_profile(
    request,
    character_id,
):
    profile = get_character_profile(
        character_id=character_id,
    )

    if not profile:

        return JsonResponse(
            {
                "profile": None,
            }
        )

    return JsonResponse(
        {
            "profile": {
                "personality_notes": (
                    profile.personality_notes
                ),
                "age_range": (
                    profile.age_range
                ),
                "gender": (
                    profile.gender
                ),
                "nationality": (
                    profile.nationality
                ),
            }
        }
    )