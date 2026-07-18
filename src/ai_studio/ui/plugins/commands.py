class CommandRegistry:

    def __init__(self):
        self._commands = {}

    def register(
        self,
        name,
        callback,
    ):
        self._commands[name] = callback

    def execute(
        self,
        name,
    ):
        self._commands[name]()