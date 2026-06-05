from apps.stories.models import SceneCharacter


def get_scene_characters(
    scene_id,
):
    return (
        SceneCharacter.objects
        .select_related(
            "character",
        )
        .filter(
            scene_id=scene_id,
        )
    )