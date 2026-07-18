from __future__ import annotations

from .manager import PluginManager
from .registry import register_builtin


class PluginLoader:
    """Loads built-in plugins."""

    def __init__(self, manager: PluginManager) -> None:
        self._manager = manager

    def load(self) -> None:
        register_builtin(self._manager)