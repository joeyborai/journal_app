from datetime import date

from journal_backend.models import JournalEntry


def get_journal_entry_for_date(date: date) -> JournalEntry:
  return JournalEntry.objects.filter(
    date_entered=date
  ).prefetch_related(
    'entrytag_set',
    'entrytag_set__tag_type'
  )


def get_all_journal_entries_for_user_id(user_id: int) -> list[JournalEntry]:
  return JournalEntry.objects.filter(
    user_id=user_id
  ).prefetch_related(
    'entrytag_set',
    'entrytag_set__tag_type'
  ).all()
