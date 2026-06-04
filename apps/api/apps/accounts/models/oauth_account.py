from django.db import models

from shared.database.base_model import BaseModel


class OAuthAccount(BaseModel):

    PROVIDERS = [
        ("google", "Google"),
        ("github", "GitHub"),
        ("apple", "Apple"),
        ("microsoft", "Microsoft"),
    ]

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="oauth_accounts",
    )

    provider = models.CharField(
        max_length=50,
        choices=PROVIDERS,
    )

    provider_account_id = models.CharField(
        max_length=255,
        db_index=True,
    )

    provider_email = models.EmailField(
        blank=True,
    )

    class Meta:
        db_table = "oauth_accounts"

        unique_together = (
            "provider",
            "provider_account_id",
        )