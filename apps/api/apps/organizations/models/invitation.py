import uuid

from django.db import models

from .membership import Membership

from shared.database.base_model import BaseModel


class Invitation(BaseModel):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("expired", "Expired"),
        ("cancelled", "Cancelled"),
    ]

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="invitations",
    )

    email = models.EmailField(
        db_index=True,
    )

    role = models.CharField(
        max_length=20,
        choices=Membership.ROLE_CHOICES,
        default="viewer",
    )

    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    expires_at = models.DateTimeField()

    invited_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="sent_invitations",
    )

    class Meta:
        db_table = "organization_invitations"