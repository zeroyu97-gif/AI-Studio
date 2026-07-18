from __future__ import annotations

from abc import ABC, abstractmethod

from .models import ChatRequest, ChatResponse


class Provider(ABC):
    """Base interface for all AI providers."""

    name: str

    @abstractmethod
    def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """Execute a chat request."""
        raise NotImplementedError