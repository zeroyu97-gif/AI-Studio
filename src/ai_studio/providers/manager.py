from __future__ import annotations

from .base import Provider
from .exceptions import (
    ProviderAlreadyRegisteredError,
    ProviderNotFoundError,
)


class ProviderManager:
    """Registry of AI providers."""

    def __init__(self) -> None:
        self._providers: dict[str, Provider] = {}

    def register(self, provider: Provider) -> None:
        if provider.name in self._providers:
            raise ProviderAlreadyRegisteredError(
                f"Provider '{provider.name}' is already registered."
            )

        self._providers[provider.name] = provider

    def get(self, name: str) -> Provider:
        try:
            return self._providers[name]
        except KeyError as exc:
            raise ProviderNotFoundError(
                f"Provider '{name}' is not registered."
            ) from exc

    def available(self) -> list[str]:
        return sorted(self._providers.keys())