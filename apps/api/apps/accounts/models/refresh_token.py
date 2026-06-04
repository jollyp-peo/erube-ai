import uuid

from django.db import models

from shared.database.base_model import BaseModel


class RefreshToken(BaseModel):

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="refresh_tokens",
    )

    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    is_revoked = models.BooleanField(
        default=False,
    )

    expires_at = models.DateTimeField()

    user_agent = models.TextField(
        blank=True,
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "refresh_tokens"