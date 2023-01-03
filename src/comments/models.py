from django.db import models

from tickets.models import Ticket
from shared.django import TimeStampMixin
from django.conf import settings


class Comment(TimeStampMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="comments"
    )
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    body = models.TextField()
