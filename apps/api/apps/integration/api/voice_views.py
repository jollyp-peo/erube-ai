from django.http import JsonResponse

from apps.integration.selectors.voice_selector import (
    get_project_voices,
)


def internal_project_voices(
    request,
    project_id,
):
    voices = get_project_voices(
        project_id=project_id,
    )

    return JsonResponse(
        {
            "voices": [
                {
                    "id": str(voice.id),
                    "name": voice.name,
                    "description": voice.description,
                    "status": voice.status,
                }
                for voice in voices
            ]
        }
    )