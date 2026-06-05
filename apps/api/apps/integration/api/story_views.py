from django.http import JsonResponse

from apps.integration.selectors.story_selector import (
    get_story_by_id,
)


def internal_story_detail(
    request,
    story_id,
):
    story = get_story_by_id(
        story_id=story_id,
    )

    return JsonResponse(
    {
        "id": str(story.id),
        "project_id": str(story.project_id),
        "title": story.title,
        "description": story.description,
        "genre": story.genre,
        "status": story.status,
    }
)