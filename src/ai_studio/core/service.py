from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Service(Protocol):
    """Base protocol for application services."""

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...