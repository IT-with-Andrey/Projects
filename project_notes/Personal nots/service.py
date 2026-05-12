
from datetime import datetime

from typing import Optional
import uuid

from models import Note


class NotesService:
    def __init__(self, storage):
        self.storage = storage
        raw_data = self.storage.load()

        self.notes: dict[str, Note] = {
            note_id: Note.from_dict(note_date)
            for note_id, note_date in raw_data.items()
        }

    def _save(self) -> None:
        data = {
            note_id: note.to_dict()
            for note_id, note in self.notes.items()


        }
        self.storage.save(data)

    def add_note(self, title: str, text: str) -> Note:
        note = Note(
            id=str(uuid.uuid4()),
            title=title.strip(),
            text=text.strip(),
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M"),

        )

        self.notes[note.id] = note
        self._save()
        return note

    def delete_note(self, note_id: str) -> bool:
        if note_id not in self.notes:
            return False

        del self.notes[note_id]
        self._save()
        return True

    def search_notes(self, keyword: str) -> list[Note]:
        keyword = keyword.lower().strip()

        return [
            note
            for note in self.notes.values()
            if keyword in note.title.lower() or keyword in note.text.lower()
        ]

    def get_all_notes(self) -> list[Note]:
        return list(self.notes.values())
