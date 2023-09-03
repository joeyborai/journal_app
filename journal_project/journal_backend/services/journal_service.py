from datetime import date

from django.db import transaction

from journal_backend.models import JournalEntry, EntryTag, TagType


def create_journal_entry(text: str, date_entered: date, tag_ids: list[str]):
  with transaction.atomic():
    journal_entry = JournalEntry.objects.create(
      text=text,
      date_entered=date_entered
    )

    tag_types: list[TagType] = list(TagType.objects.filter(tag_id__in=tag_ids).all())
    entry_tags: list[EntryTag] = []

    for tag_type in tag_types:
      entry_tags.append(EntryTag(
        tag_type=tag_type,
        journal_entry=journal_entry
      ))

    EntryTag.objects.bulk_create(entry_tags)
