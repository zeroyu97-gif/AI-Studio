from __future__ import annotations

from typing import Any, TypeVar

from .exceptions import (
    ServiceAlreadyRegisteredError,
    ServiceNotFoundError,
)

T = TypeVar("T")


class ServiceContainer:
    """Simple dependency injection container."""

    def __init__(self) -> None:
        self._services: dict[type[Any], Any] = {}

    def register(self, interface: type[T], instance: T) -> None:
        if interface in self._services:
            raise ServiceAlreadyRegisteredError(
                f"Service '{interface.__name__}' is already registered."
            )

        self._services[interface] = instance

    def resolve(self, interface: type[T]) -> T:
        try:
            return self._services[interface]
        except KeyError as exc:
            raise ServiceNotFoundError(
                f"Service '{interface.__name__}' is not registered."
            ) from exc

    def contains(self, interface: type[Any]) -> bool:
        return interface in self._services

    def clear(self) -> None:
        self._services.clear()