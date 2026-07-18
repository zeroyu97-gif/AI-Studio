from PySide6.QtWidgets import QMainWindow


class MenuController:

    def __init__(self, window: QMainWindow):

        self.window = window

    def setup(self):

        menu = self.window.menuBar()

        file_menu = menu.addMenu("&File")
        edit_menu = menu.addMenu("&Edit")
        view_menu = menu.addMenu("&View")
        ai_menu = menu.addMenu("&AI")
        plugins_menu = menu.addMenu("&Plugins")
        help_menu = menu.addMenu("&Help")

        file_menu.addAction(self.window.action_open)
        file_menu.addAction(self.window.action_save)