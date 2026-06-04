from django.db import models

from shared.database.base_model import BaseModel


class UserSecurity(BaseModel):

    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="security",
    )

    failed_login_attempts = models.PositiveIntegerField(
        default=0,
    )

    password_changed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    last_failed_login_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    mfa_enabled = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "user_security"