from django.db import models

from journal_backend.models import BaseModel, JournalEntry
from journal_backend.models.tag_type import TagType


class EntryTag(BaseModel):
  journal_entry = models.ForeignKey(
    JournalEntry,
    on_delete=models.CASCADE
  )

  tag_type = models.ForeignKey(
    TagType,
    on_delete=models.CASCADE
  )
