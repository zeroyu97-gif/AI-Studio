from dataclasses import dataclass
from uuid import uuid4


@dataclass(slots=True)
class AgentTask:
    prompt: str
    id: str = ""

    def __post_init__(self) -> None:
        if not self.id:
            self.id = str(uuid4())