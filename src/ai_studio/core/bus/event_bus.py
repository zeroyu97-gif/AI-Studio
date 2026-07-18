from __future__ import annotations

from collections import defaultdict


class EventBus:

    def __init__(self):

        self._handlers = defaultdict(list)

    # ---------------------------------------------

    def subscribe(
        self,
        event_type,
        callback,
    ):

        self._handlers[event_type].append(
            callback
        )

    # ---------------------------------------------

    def publish(
        self,
        event,
    ):

        for callback in self._handlers.get(
            type(event),
            [],
        ):
            callback(event)