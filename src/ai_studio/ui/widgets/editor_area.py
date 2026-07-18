from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QMessageBox,
    QTabWidget,
)

from .editor import Editor


class EditorArea(QTabWidget):
    """
    Менеджер вкладок редактора.
    """

    currentEditorChanged = Signal(Editor)
    fileOpened = Signal(Path)
    fileClosed = Signal(Path)

    def __init__(self) -> None:
        super().__init__()

        self.setTabsClosable(True)
        self.setMovable(True)
        self.setDocumentMode(True)

        self.tabCloseRequested.connect(self.close_tab)
        self.currentChanged.connect(self._on_current_changed)

    # ------------------------------------------------------------
    # Open
    # ------------------------------------------------------------

    def open_file(self, path: Path) -> Editor:

        path = path.resolve()

        # Уже открыт?
        for i in range(self.count()):

            editor = self.widget(i)

            if (
                isinstance(editor, Editor)
                and editor.path == path
            ):
                self.setCurrentIndex(i)
                return editor

        editor = Editor()
        editor.load_file(path)

        editor.modifiedChanged.connect(
            lambda modified,
            e=editor: self._update_tab_title(e)
        )

        index = self.addTab(
            editor,
            editor.file_name,
        )

        self.setCurrentIndex(index)

        self.fileOpened.emit(path)

        return editor

    # ------------------------------------------------------------
    # Save
    # ------------------------------------------------------------

    def save_current(self) -> bool:

        editor = self.current_editor()

        if editor is None:
            return False

        ok = editor.save()

        if ok:
            self._update_tab_title(editor)

        return ok

    def save_all(self) -> None:

        for i in range(self.count()):

            editor = self.widget(i)

            if isinstance(editor, Editor):
                editor.save()

                self._update_tab_title(editor)

    # ------------------------------------------------------------
    # Close
    # ------------------------------------------------------------

    def close_tab(self, index: int) -> None:

        editor = self.widget(index)

        if not isinstance(editor, Editor):
            self.removeTab(index)
            return

        if editor.is_modified:

            answer = QMessageBox.question(
                self,
                "Unsaved changes",
                f"Save '{editor.file_name}' ?",
                QMessageBox.Yes
                | QMessageBox.No
                | QMessageBox.Cancel,
            )

            if answer == QMessageBox.Cancel:
                return

            if answer == QMessageBox.Yes:
                editor.save()

        if editor.path is not None:
            self.fileClosed.emit(editor.path)

        self.removeTab(index)

    def close_all(self) -> None:

        while self.count():
            self.close_tab(0)

    # ------------------------------------------------------------
    # Current
    # ------------------------------------------------------------

    def current_editor(self) -> Editor | None:

        widget = self.currentWidget()

        if isinstance(widget, Editor):
            return widget

        return None

    def opened_files(self) -> list[Path]:

        result: list[Path] = []

        for i in range(self.count()):

            editor = self.widget(i)

            if (
                isinstance(editor, Editor)
                and editor.path is not None
            ):
                result.append(editor.path)

        return result

    # ------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------

    def _update_tab_title(
        self,
        editor: Editor,
    ) -> None:

        for i in range(self.count()):

            if self.widget(i) is editor:

                title = editor.file_name

                if editor.is_modified:
                    title += " *"

                self.setTabText(
                    i,
                    title,
                )

                return

    def _on_current_changed(
        self,
        index: int,
    ) -> None:

        editor = self.current_editor()

        if editor is not None:
            self.currentEditorChanged.emit(editor)