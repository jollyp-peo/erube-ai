from django.urls import path

from .story_views import internal_story_detail
from .scene_views import internal_story_scenes
from .shot_views import internal_scene_shots
from .character_views import (
    internal_project_characters,
)

from .voice_views import (
    internal_project_voices,
)
from .scene_character_views import internal_scene_characters

urlpatterns = [
    path(
        "internal/stories/<uuid:story_id>/",
        internal_story_detail,
        name="internal-story-detail",
    ),

    path(
        "internal/stories/<uuid:story_id>/scenes/",
        internal_story_scenes,
        name="internal-story-scenes",
    ),

    path(
        "internal/scenes/<uuid:scene_id>/shots/",
        internal_scene_shots,
        name="internal-scene-shots",
    ),
    path(
    "internal/projects/<uuid:project_id>/characters/",
    internal_project_characters,
    name="internal-project-characters",
    ),

    path(
    "internal/projects/<uuid:project_id>/voices/",
    internal_project_voices,
    name="internal-project-voices",
   ),
    
    path(
    "internal/scenes/<uuid:scene_id>/characters/",
    internal_scene_characters,
    name="internal-scene-characters",
),
]