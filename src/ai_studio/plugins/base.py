from __future__ import annotations

from typing import Protocol


class Plugin(Protocol):

    name: str
    version: str

    def load(self) -> None:
        ...

    def unload(self) -> None:
        ...