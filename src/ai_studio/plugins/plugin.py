from __future__ import annotations

from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Base plugin.
    """

    id = "plugin"
    name = "Plugin"
    version = "1.0"

    def __init__(self, context):
        self.context = context

    @abstractmethod
    def activate(self):
        ...

    def deactivate(self):
        pass