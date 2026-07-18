from collections.abc import Callable


class CommandBus:

    def __init__(self):
        self._handlers = {}

    def register(
        self,
        command,
        handler,
    ):
        self._handlers[command] = handler

    def execute(self, command):

        handler = self._handlers[type(command)]

        return handler(command)