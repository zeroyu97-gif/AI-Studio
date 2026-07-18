from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtGui import QTextCursor, QTextOption
from PySide6.QtWidgets import QPlainTextEdit

from .python_highlighter import PythonHighlighter


class Editor(QPlainTextEdit):
    """
    Редактор исходного кода.
    """

    modifiedChanged = Signal(bool)
    cursorPositionChangedEx = Signal(int, int)

    def __init__(self) -> None:
        super().__init__()

        self.path: Path | None = None

        self.setWordWrapMode(QTextOption.NoWrap)
        self.setTabStopDistance(40)

        self.highlighter = PythonHighlighter(
            self.document()
        )

        self.document().modificationChanged.connect(
            self.modifiedChanged.emit
        )

        self.cursorPositionChanged.connect(
            self._cursor_changed
        )

    # --------------------------------------------------------
    # Cursor
    # --------------------------------------------------------

    def _cursor_changed(self) -> None:

        cursor = self.textCursor()

        self.cursorPositionChangedEx.emit(
            cursor.blockNumber() + 1,
            cursor.columnNumber() + 1,
        )

    # --------------------------------------------------------
    # File
    # --------------------------------------------------------

    def load_file(self, path: Path) -> None:

        self.path = path

        self.setPlainText(
            path.read_text(
                encoding="utf-8"
            )
        )

        self.document().setModified(False)

    def save(self) -> bool:

        if self.path is None:
            return False

        self.path.write_text(
            self.toPlainText(),
            encoding="utf-8",
        )

        self.document().setModified(False)

        return True

    # --------------------------------------------------------
    # Helpers
    # --------------------------------------------------------

    @property
    def file_name(self) -> str:

        if self.path is None:
            return "Untitled"

        return self.path.name

    @property
    def is_modified(self) -> bool:

        return self.document().isModified()

    @property
    def current_line(self) -> int:

        return self.textCursor().blockNumber() + 1

    @property
    def current_column(self) -> int:

        return self.textCursor().columnNumber() + 1

    def goto_line(
        self,
        line: int,
    ) -> None:

        cursor = QTextCursor(
            self.document().findBlockByLineNumber(
                max(0, line - 1)
            )
        )

        self.setTextCursor(cursor)
        self.centerCursor()