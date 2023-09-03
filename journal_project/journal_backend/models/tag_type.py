from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy

from journal_backend.models import BaseModel


class TagType(BaseModel):
  class TagCategories(models.TextChoices):
    PEOPLE = 'people', gettext_lazy('People')
    ACTIVITIES = 'activities', gettext_lazy('Activities')

  user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
  )

  category = models.CharField(
    max_length=100,
    choices=TagCategories.choices,
  )

  text = models.CharField(
    max_length=100
  )
