import importlib


class PluginLoader:

    def load(self, module_name):

        module = importlib.import_module(module_name)

        return module.Plugin