from __future__ import annotations

from .base import Plugin


class PluginManager:

    def __init__(self) -> None:
        self._plugins: dict[str, Plugin] = {}

    def register(self, plugin: Plugin) -> None:
        self._plugins[plugin.name] = plugin

    def load_all(self) -> None:
        for plugin in self._plugins.values():
            plugin.load()

    def unload_all(self) -> None:
        for plugin in reversed(list(self._plugins.values())):
            plugin.unload()

    @property
    def plugins(self) -> tuple[Plugin, ...]:
        return tuple(self._plugins.values())