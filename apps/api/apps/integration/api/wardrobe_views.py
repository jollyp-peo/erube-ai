from django.http import JsonResponse

from apps.integration.selectors.wardrobe_selector import (
    get_scene_wardrobes,
)


def internal_scene_wardrobes(
    request,
    scene_id,
):
    assignments = get_scene_wardrobes(
        scene_id=scene_id,
    )

    return JsonResponse(
        {
            "wardrobes": [
                {
                    "character_id": str(
                        item.character.id
                    ),
                    "character_name": (
                        item.character.name
                    ),
                    "wardrobe_id": str(
                        item.wardrobe.id
                    ),
                    "wardrobe_name": (
                        item.wardrobe.name
                    ),
                }
                for item in assignments
            ]
        }
    )