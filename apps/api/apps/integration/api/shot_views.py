from django.http import JsonResponse

from apps.integration.selectors.shot_selector import (
    get_scene_shots,
)


def internal_scene_shots(
    request,
    scene_id,
):
    shots = get_scene_shots(
        scene_id=scene_id,
    )

    return JsonResponse(
        {
            "shots": [
                {
                    "id": str(shot.id),
                    "shot_number": shot.shot_number,
                    "title": shot.title,
                    "description": shot.description,
                    "camera_type": shot.camera_type,
                    "camera_movement": shot.camera_movement,
                    "duration_seconds": shot.duration_seconds,
                }
                for shot in shots
            ]
        }
    )