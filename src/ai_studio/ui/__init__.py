class MainWindow(QMainWindow):

    def __init__(self):

        ...

        self._create_actions()
        self._create_menu()
        self._create_toolbar()
        self._create_workspace()
        self._create_ai()
        self._create_plugins()
        self._restore_session()