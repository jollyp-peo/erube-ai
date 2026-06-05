from apps.characters.models import Character


def get_project_characters(
    project_id,
):
    return Character.objects.filter(
        project_id=project_id,
    )