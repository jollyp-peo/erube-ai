from apps.stories.models import Shot


def get_scene_shots(
    scene_id,
):
    return Shot.objects.filter(
        scene_id=scene_id
    ).order_by(
        "shot_number"
    )