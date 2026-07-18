class ToolbarController:

    def __init__(self, window):

        self.window = window

    def setup(self):

        toolbar = self.window.addToolBar("Main")

        toolbar.addAction(self.window.action_open)
        toolbar.addAction(self.window.action_save)

        self.window.toolbar = toolbar