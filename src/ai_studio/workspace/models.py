from dataclasses import dataclass


@dataclass(slots=True)
class ChatRequest:
    prompt: str
    system_prompt: str | None = None
    model: str | None = None


@dataclass(slots=True)
class ChatResponse:
    text: str
    provider: str
    model: str | None = None