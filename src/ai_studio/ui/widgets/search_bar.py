from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)


class SearchBar(QWidget):
    """
    Панель поиска и замены.
    """

    searchRequested = Signal(
        str,
        bool,   # next
        bool,   # case sensitive
        bool,   # regex
    )

    replaceRequested = Signal(
        str,
        str,
    )

    replaceAllRequested = Signal(
        str,
        str,
    )

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)

        # -----------------------------
        # Search
        # -----------------------------

        layout.addWidget(QLabel("Find"))

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search...")

        layout.addWidget(self.search, 2)

        # -----------------------------
        # Replace
        # -----------------------------

        layout.addWidget(QLabel("Replace"))

        self.replace = QLineEdit()
        self.replace.setPlaceholderText("Replace...")

        layout.addWidget(self.replace, 2)

        # -----------------------------
        # Options
        # -----------------------------

        self.case = QCheckBox("Aa")
        self.regex = QCheckBox(".*")

        layout.addWidget(self.case)
        layout.addWidget(self.regex)

        # -----------------------------
        # Buttons
        # -----------------------------

        self.previous = QPushButton("◀")
        self.next = QPushButton("▶")
        self.replace_one = QPushButton("Replace")
        self.replace_all = QPushButton("All")

        layout.addWidget(self.previous)
        layout.addWidget(self.next)
        layout.addWidget(self.replace_one)
        layout.addWidget(self.replace_all)

        # -----------------------------
        # Shortcuts
        # -----------------------------

        self.search.returnPressed.connect(
            self.find_next
        )

        self.next.clicked.connect(
            self.find_next
        )

        self.previous.clicked.connect(
            self.find_previous
        )

        self.replace_one.clicked.connect(
            self.replace_current
        )

        self.replace_all.clicked.connect(
            self.replace_everything
        )

    # -----------------------------------------------------

    def pattern(self) -> str:
        return self.search.text()

    def replacement(self) -> str:
        return self.replace.text()

    # -----------------------------------------------------

    def find_next(self):

        self.searchRequested.emit(
            self.pattern(),
            True,
            self.case.isChecked(),
            self.regex.isChecked(),
        )

    def find_previous(self):

        self.searchRequested.emit(
            self.pattern(),
            False,
            self.case.isChecked(),
            self.regex.isChecked(),
        )

    # -----------------------------------------------------

    def replace_current(self):

        self.replaceRequested.emit(
            self.pattern(),
            self.replacement(),
        )

    def replace_everything(self):

        self.replaceAllRequested.emit(
            self.pattern(),
            self.replacement(),
        )

    # -----------------------------------------------------

    def focus_search(self):

        self.search.setFocus(
            Qt.ShortcutFocusReason
        )

        self.search.selectAll()