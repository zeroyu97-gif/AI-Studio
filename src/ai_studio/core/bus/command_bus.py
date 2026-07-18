from __future__ import annotations

from collections import defaultdict


class CommandBus:

    def __init__(self):

        self._handlers = {}

    # ---------------------------------------------

    def register(
        self,
        command_type,
        handler,
    ):

        self._handlers[command_type] = handler

    # ---------------------------------------------

    def dispatch(
        self,
        command,
    ):

        handler = self._handlers.get(
            type(command)
        )

        if handler is None:
            return

        return handler(command)