from django.http import JsonResponse

from apps.integration.selectors.scene_selector import (
    get_story_scenes,
)


def internal_story_scenes(
    request,
    story_id,
):
    scenes = get_story_scenes(
        story_id=story_id,
    )

    return JsonResponse(
        {
            "scenes": [
                {
                    "id": str(scene.id),
                    "title": scene.title,
                    "scene_number": scene.scene_number,
                    "summary": scene.summary,
                    "location": scene.location,
                    "time_of_day": scene.time_of_day,
                    "duration_estimate": scene.duration_estimate,
                }
                for scene in scenes
            ]
        }
    )