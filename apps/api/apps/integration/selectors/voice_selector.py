from apps.voices.models import Voice


def get_project_voices(
    project_id,
):
    return Voice.objects.filter(
        project_id=project_id,
    )