from django.db import models
from django.conf import settings

from journal_backend.models import BaseModel


class JournalEntry(BaseModel):
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
  )

  text = models.CharField(
    max_length=2000,
    null=False
  )

  date_entered = models.DateField(
    auto_now=True,
    null=False,
  )
