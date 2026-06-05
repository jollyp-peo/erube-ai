from apps.stories.models import Story


def get_story_by_id(
    story_id: str,
):
    return Story.objects.select_related(
        "project",
        "created_by",
    ).get(
        id=story_id,
    )