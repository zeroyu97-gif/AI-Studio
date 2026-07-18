from dataclasses import dataclass
@dataclass(slots=True)
class ChatResponse:
    message: str
    provider: str
    model: str | None = None
    finish_reason: str | None = None