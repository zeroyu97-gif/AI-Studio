from __future__ import annotations

from .plugin import UIPlugin


class UIPluginManager:
    def __init__(self) -> None:
        self._plugins: dict[str, UIPlugin] = {}

    def register(self, plugin: UIPlugin) -> None:
        if plugin.name in self._plugins:
            raise ValueError(
                f"Plugin '{plugin.name}' is already registered."
            )

        self._plugins[plugin.name] = plugin

    def load(self, window) -> None:
        for plugin in self._plugins.values():
            plugin.setup(window)