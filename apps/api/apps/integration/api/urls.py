from django.urls import path

from .story_views import internal_story_detail
from .scene_views import internal_story_scenes
from .shot_views import internal_scene_shots


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
]