

from dataclasses import dataclass , asdict

from datetime import datetime

from turtle import title
from typing import Any


@dataclass
class Note:
    id: str
    title: str
    text: str
    created_at :str


    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    
    @classmethod
    def from_dict(cls , data: dict[str,Any]) -> 'Note':
        return cls(
            id=data['id'],
            title=data['title'],
            text=data['text'],
           created_at=data["created_at"]
        )
