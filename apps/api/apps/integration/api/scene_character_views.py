from django.http import JsonResponse

from apps.integration.selectors.scene_character_selector import (
    get_scene_characters,
)


def internal_scene_characters(
    request,
    scene_id,
):
    scene_characters = get_scene_characters(
        scene_id=scene_id,
    )

    return JsonResponse(
        {
            "characters": [
                {
                    "character_id": str(
                        item.character.id
                    ),
                    "name": item.character.name,
                    "role_name": item.role_name,
                    "is_speaking": item.is_speaking,
                    "importance": item.importance,
                }
                for item in scene_characters
            ]
        }
    )