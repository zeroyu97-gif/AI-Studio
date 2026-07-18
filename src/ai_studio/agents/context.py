from dataclasses import dataclass


@dataclass(slots=True)
class AgentContext:
    project: str | None = None
    active_file: str | None = None