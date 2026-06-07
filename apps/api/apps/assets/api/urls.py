from django.urls import path

from .internal_views import (
    create_asset,
)

urlpatterns = [
    path(
        "internal/assets/",
        create_asset,
    ),
]