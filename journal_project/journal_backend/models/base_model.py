from typing import Any, Union

from django.db import models


class BaseModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)

  def save(self,
           force_insert: bool = False,
           force_update: bool = False,
           using: Any = None,
           update_fields: Union[list[str], tuple[str]] | None = None) -> None:
    # enforce 'updated_at' is included when update_fields is specified without it
    if update_fields is not None and 'updated_at' not in update_fields:
      update_fields = set(update_fields)
      update_fields.add('updated_at')
    super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

  class Meta:
    abstract = True
