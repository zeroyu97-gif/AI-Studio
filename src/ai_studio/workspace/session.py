from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(slots=True)
class Session:
    id: str = field(default_factory=lambda: str(uuid4()))
    opened_files: list[str] = field(default_factory=list)
    active_file: str | None = None