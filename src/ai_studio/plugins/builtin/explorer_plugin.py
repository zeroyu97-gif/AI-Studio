from plugins.plugin import Plugin


class Plugin(Plugin):

    id = "explorer"

    name = "Explorer"

    version = "1.0"

    def activate(self):

        print("Explorer loaded")

    def deactivate(self):

        print("Explorer unloaded")