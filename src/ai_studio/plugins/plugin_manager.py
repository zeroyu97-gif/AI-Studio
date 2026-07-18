from .plugin_loader import PluginLoader
from .plugin_registry import PluginRegistry


class PluginManager:

    def __init__(self, context):

        self.context = context

        self.loader = PluginLoader()

        self.registry = PluginRegistry()

    def load(self, module):

        cls = self.loader.load(module)

        plugin = cls(self.context)

        plugin.activate()

        self.registry.register(plugin)

        return plugin

    def unload(self, plugin_id):

        plugin = self.registry.get(plugin_id)

        if plugin is None:
            return

        plugin.deactivate()

        self.registry.unregister(plugin_id)

    def plugins(self):

        return self.registry.all()