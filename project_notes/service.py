

from datetime import datetime
from typing import Optional
import uuid


from models import Note



class NotesService:

    def __init__(self, storage):
        self.storage = storage
        raw_data = self.storage.load()

        self.notes: dict[str,Note] = {
            note_id: Note.from_dict(note_data)
            for note_id, note_data in raw_data.items()
                           
                            }
    
    def _save(self) -> None:
        data = {
            note_id: note.to_dict()
            for note_id , note in self.notes.items()
        }
        self.storage.save(data)