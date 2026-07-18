from __future__ import annotations

from .manager import PluginManager
from .system.plugin import SystemPlugin


def register_builtin(manager: PluginManager) -> None:
    """Register built-in plugins."""
    manager.register(SystemPlugin())