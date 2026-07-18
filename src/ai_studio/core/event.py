from dataclasses import dataclass
from datetime import datetime, UTC
from uuid import uuid4


@dataclass(slots=True)
class Event:
    event_id: str = ""
    created_at: datetime | None = None

    def __post_init__(self) -> None:
        if not self.event_id:
            self.event_id = str(uuid4())

        if self.created_at is None:
            self.created_at = datetime.now(UTC)