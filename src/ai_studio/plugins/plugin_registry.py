class PluginRegistry:

    def __init__(self):

        self.plugins = {}

    def register(self, plugin):

        self.plugins[plugin.id] = plugin

    def unregister(self, plugin_id):

        self.plugins.pop(plugin_id, None)

    def all(self):

        return list(self.plugins.values())

    def get(self, plugin_id):

        return self.plugins.get(plugin_id)
