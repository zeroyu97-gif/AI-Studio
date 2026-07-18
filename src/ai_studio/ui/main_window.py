from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QCloseEvent
from PySide6.QtWidgets import (
    QFileDialog,
    QDockWidget,
    QMainWindow,
    QMessageBox,
    QStatusBar,
    QToolBar,
    QWidget,
)

from .widgets.editor_area import EditorArea
from .widgets.explorer import Explorer


class MainWindow(QMainWindow):
    """
    Main application window.

    MainWindow only coordinates the UI.

    Business logic is delegated to managers/controllers.
    """

    def __init__(self, parent=None):

        super().__init__(parent)

        self.current_project: Path | None = None

        self.editor: EditorArea | None = None
        self.explorer: Explorer | None = None

        self.toolbar: QToolBar | None = None
        self.status: QStatusBar | None = None

        self.explorer_dock: QDockWidget | None = None
        self.problems_dock: QDockWidget | None = None
        self.terminal_dock: QDockWidget | None = None
        self.ai_dock: QDockWidget | None = None
        self.git_dock: QDockWidget | None = None

        self._configure_window()

        self._create_actions()
        self._create_menu()
        self._create_toolbar()

        self._create_statusbar()

        self._create_central_widgets()
        self._create_docks()

        self._connect_signals()

        self._restore_window_state()
     # --------------------------------------------------
    # Window
    # --------------------------------------------------

    def _configure_window(self):

        self.setWindowTitle("AI Studio")

        self.resize(1700, 950)

        self.setMinimumSize(
            QSize(1280, 720)
        )

        self.setDockNestingEnabled(True)

        self.setAnimated(True)

        self.setUnifiedTitleAndToolBarOnMac(False)
            # --------------------------------------------------
    # Restore State
    # --------------------------------------------------

    def _restore_window_state(self):

        """
        Later this will restore

        geometry

        docks

        session

        workspace

        open files

        terminal

        etc.
        """

        pass
    # --------------------------------------------------
# Actions
# --------------------------------------------------

def _create_actions(self):

    #
    # File
    #

    self.action_new = QAction("New File", self)
    self.action_new.setShortcut("Ctrl+N")

    self.action_open = QAction("Open Project...", self)
    self.action_open.setShortcut("Ctrl+O")

    self.action_open_file = QAction("Open File...", self)
    self.action_open_file.setShortcut("Ctrl+Shift+O")

    self.action_save = QAction("Save", self)
    self.action_save.setShortcut("Ctrl+S")

    self.action_save_as = QAction("Save As...", self)
    self.action_save_as.setShortcut("Ctrl+Shift+S")

    self.action_close = QAction("Close", self)
    self.action_close.setShortcut("Ctrl+W")

    self.action_exit = QAction("Exit", self)
    self.action_exit.setShortcut("Ctrl+Q")

    #
    # Edit
    #

    self.action_undo = QAction("Undo", self)
    self.action_undo.setShortcut("Ctrl+Z")

    self.action_redo = QAction("Redo", self)
    self.action_redo.setShortcut("Ctrl+Shift+Z")

    self.action_cut = QAction("Cut", self)
    self.action_cut.setShortcut("Ctrl+X")

    self.action_copy = QAction("Copy", self)
    self.action_copy.setShortcut("Ctrl+C")

    self.action_paste = QAction("Paste", self)
    self.action_paste.setShortcut("Ctrl+V")

    #
    # View
    #

    self.action_toggle_explorer = QAction(
        "Explorer",
        self,
    )

    self.action_toggle_explorer.setCheckable(True)
    self.action_toggle_explorer.setChecked(True)

    self.action_toggle_terminal = QAction(
        "Terminal",
        self,
    )

    self.action_toggle_terminal.setCheckable(True)

    self.action_toggle_problems = QAction(
        "Problems",
        self,
    )

    self.action_toggle_problems.setCheckable(True)

    self.action_toggle_ai = QAction(
        "AI Assistant",
        self,
    )

    self.action_toggle_ai.setCheckable(True)

    self.action_toggle_git = QAction(
        "Git",
        self,
    )

    self.action_toggle_git.setCheckable(True)
    # --------------------------------------------------
# Menu
# --------------------------------------------------

def _create_menu(self):

    menu = self.menuBar()

    #
    # File
    #

    file_menu = menu.addMenu("&File")

    file_menu.addAction(self.action_new)
    file_menu.addSeparator()

    file_menu.addAction(self.action_open)
    file_menu.addAction(self.action_open_file)

    file_menu.addSeparator()

    file_menu.addAction(self.action_save)
    file_menu.addAction(self.action_save_as)

    file_menu.addSeparator()

    file_menu.addAction(self.action_close)

    file_menu.addSeparator()

    file_menu.addAction(self.action_exit)

    #
    # Edit
    #

    edit_menu = menu.addMenu("&Edit")

    edit_menu.addAction(self.action_undo)
    edit_menu.addAction(self.action_redo)

    edit_menu.addSeparator()

    edit_menu.addAction(self.action_cut)
    edit_menu.addAction(self.action_copy)
    edit_menu.addAction(self.action_paste)

    #
    # View
    #

    view_menu = menu.addMenu("&View")

    view_menu.addAction(self.action_toggle_explorer)
    view_menu.addAction(self.action_toggle_terminal)
    view_menu.addAction(self.action_toggle_problems)
    view_menu.addAction(self.action_toggle_git)
    view_menu.addAction(self.action_toggle_ai)
    # --------------------------------------------------
# Toolbar
# --------------------------------------------------

def _create_toolbar(self):

    self.toolbar = QToolBar("Main")

    self.toolbar.setObjectName("MainToolbar")

    self.toolbar.setMovable(False)

    self.toolbar.setIconSize(QSize(18, 18))

    self.addToolBar(
        Qt.TopToolBarArea,
        self.toolbar,
    )

    self.toolbar.addAction(self.action_new)

    self.toolbar.addSeparator()

    self.toolbar.addAction(self.action_open)

    self.toolbar.addSeparator()

    self.toolbar.addAction(self.action_save)

    self.toolbar.addSeparator()

    self.toolbar.addAction(self.action_undo)
    self.toolbar.addAction(self.action_redo)
    # --------------------------------------------------
# StatusBar
# --------------------------------------------------

def _create_statusbar(self):

    self.status = QStatusBar()

    self.setStatusBar(self.status)

    self.status.showMessage("Ready")

    self.cursor_label = QLabel("Ln 1, Col 1")

    self.encoding_label = QLabel("UTF-8")

    self.language_label = QLabel("Python")

    self.status.addPermanentWidget(
        self.language_label
    )

    self.status.addPermanentWidget(
        self.encoding_label
    )

    self.status.addPermanentWidget(
        self.cursor_label
    )
    # --------------------------------------------------
# Central Widget
# --------------------------------------------------

def _create_central_widgets(self):

    self.editor = EditorArea()

    self.setCentralWidget(
        self.editor
    )
    self.explorer = Explorer()

self.explorer_dock = QDockWidget(
    "Explorer",
    self,
)

self.explorer_dock.setObjectName(
    "ExplorerDock"
)

self.explorer_dock.setWidget(
    self.explorer
)

self.addDockWidget(
    Qt.LeftDockWidgetArea,
    self.explorer_dock,
)
from PySide6.QtWidgets import QListWidget

self.problems = QListWidget()

self.problems_dock = QDockWidget(
    "Problems",
    self,
)

self.problems_dock.setWidget(
    self.problems
)

self.addDockWidget(
    Qt.BottomDockWidgetArea,
    self.problems_dock,
)

self.problems_dock.hide()
from PySide6.QtWidgets import QTextEdit

self.terminal = QTextEdit()

self.terminal.setReadOnly(True)

self.terminal_dock = QDockWidget(
    "Terminal",
    self,
)

self.terminal_dock.setWidget(
    self.terminal
)

self.addDockWidget(
    Qt.BottomDockWidgetArea,
    self.terminal_dock,
)

self.terminal_dock.hide()self.ai_panel = QTextEdit()

self.ai_panel.setPlaceholderText(
    "AI Assistant"
)

self.ai_dock = QDockWidget(
    "AI",
    self,
)

self.ai_dock.setWidget(
    self.ai_panel
)

self.addDockWidget(
    Qt.RightDockWidgetArea,
    self.ai_dock,
)

self.ai_dock.hide()
self.git_panel = QListWidget()

self.git_dock = QDockWidget(
    "Git",
    self,
)

self.git_dock.setWidget(
    self.git_panel
)

self.addDockWidget(
    Qt.BottomDockWidgetArea,
    self.git_dock,
)

self.git_dock.hide()
self.tabifyDockWidget(

    self.problems_dock,

    self.terminal_dock,

)

self.tabifyDockWidget(

    self.terminal_dock,

    self.git_dock,

)
# --------------------------------------------------
# Signals
# --------------------------------------------------

def _connect_signals(self):

    self.action_open.triggered.connect(
        self.open_project
    )

    self.action_save.triggered.connect(
        self.save_file
    )

    self.action_exit.triggered.connect(
        self.close
    )

    self.action_toggle_explorer.toggled.connect(
        self.explorer_dock.setVisible
    )

    self.action_toggle_terminal.toggled.connect(
        self.terminal_dock.setVisible
    )

    self.action_toggle_problems.toggled.connect(
        self.problems_dock.setVisible
    )

    self.action_toggle_git.toggled.connect(
        self.git_dock.setVisible
    )

    self.action_toggle_ai.toggled.connect(
        self.ai_dock.setVisible
    )