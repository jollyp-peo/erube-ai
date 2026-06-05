from django.http import JsonResponse

from apps.integration.selectors.character_selector import (
    get_project_characters,
)


def internal_project_characters(
    request,
    project_id,
):
    characters = get_project_characters(
        project_id=project_id,
    )

    return JsonResponse(
        {
            "characters": [
                {
                    "id": str(character.id),
                    "name": character.name,
                    "description": character.description,
                    "status": character.status,
                }
                for character in characters
            ]
        }
    )