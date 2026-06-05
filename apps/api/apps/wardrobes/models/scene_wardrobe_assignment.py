from django.db import models

from shared.database.base_model import BaseModel


class SceneWardrobeAssignment(BaseModel):

    scene = models.ForeignKey(
        "stories.Scene",
        on_delete=models.CASCADE,
        related_name="wardrobe_assignments",
    )

    character = models.ForeignKey(
        "characters.Character",
        on_delete=models.CASCADE,
    )

    wardrobe = models.ForeignKey(
        "wardrobes.Wardrobe",
        on_delete=models.CASCADE,
    )

    class Meta:

        db_table = "scene_wardrobe_assignments"