from apps.stories.models import Scene


def get_story_scenes(
    story_id,
):
    return Scene.objects.filter(
        story_id=story_id
    ).order_by(
        "scene_number"
    )