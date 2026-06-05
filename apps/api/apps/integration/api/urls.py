from django.urls import path

from .story_views import (
    internal_story_detail,
)

urlpatterns = [
    path(
        "internal/stories/<uuid:story_id>/",
        internal_story_detail,
        name="internal-story-detail",
    ),
]