import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.assets.models import Asset


@csrf_exempt
def create_asset(request):

    if request.method != "POST":

        return JsonResponse(
            {
                "error": "POST required"
            },
            status=405,
        )

    data = json.loads(
        request.body
    )

    asset = Asset.objects.create(
        project_id=data[
            "project_id"
        ],
        name=data["name"],
        asset_type=data[
            "asset_type"
        ],
        file_url=data[
            "file_url"
        ],
    )

    return JsonResponse(
        {
            "asset_id": str(asset.id),
        }
    )