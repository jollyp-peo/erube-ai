from apps.wardrobes.models import (
    SceneWardrobeAssignment,
)


def get_scene_wardrobes(
    scene_id,
):
    return (
        SceneWardrobeAssignment.objects
        .select_related(
            "character",
            "wardrobe",
        )
        .filter(
            scene_id=scene_id,
        )
    )