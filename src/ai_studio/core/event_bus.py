from __future__ import annotations

import logging
from collections import defaultdict
from collections.abc import Callable

from .event import Event

logger = logging.getLogger(__name__)

EventHandler = Callable[[Event], None]


class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[type[Event], list[EventHandler]] = defaultdict(list)

    def subscribe(
        self,
        event_type: type[Event],
        handler: EventHandler,
    ) -> None:
        self._handlers[event_type].append(handler)

    def unsubscribe(
        self,
        event_type: type[Event],
        handler: EventHandler,
    ) -> None:
        handlers = self._handlers.get(event_type)

        if handlers and handler in handlers:
            handlers.remove(handler)

    def publish(self, event: Event) -> None:
        for handler in list(self._handlers.get(type(event), [])):
            try:
                handler(event)
            except Exception:
                logger.exception(
                    "Event handler failed: %s",
                    handler,
                )

    def clear(self) -> None:
        self._handlers.clear()