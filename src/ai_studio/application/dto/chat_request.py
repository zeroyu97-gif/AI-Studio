from dataclasses import dataclass


@dataclass(slots=True)
class ChatRequest:
    message: str
    session_id: str | None = None