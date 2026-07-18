from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import (
    QDir,
    QModelIndex,
    Qt,
)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileSystemModel


class ExplorerModel(QFileSystemModel):
    """
    Модель файловой системы для Project Explorer.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setRootPath("")

        self.setResolveSymlinks(True)
        self.setReadOnly(False)

        self.setFilter(
            QDir.AllDirs
            | QDir.Files
            | QDir.NoDotAndDotDot
        )

        self._show_hidden = False

    # ---------------------------------------------------------
    # Hidden files
    # ---------------------------------------------------------

    def show_hidden(self, enabled: bool) -> None:

        self._show_hidden = enabled

        flags = (
            QDir.AllDirs
            | QDir.Files
            | QDir.NoDotAndDotDot
        )

        if enabled:
            flags |= QDir.Hidden

        self.setFilter(flags)

    @property
    def hidden_visible(self) -> bool:
        return self._show_hidden

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def path(self, index: QModelIndex) -> Path:
        return Path(self.filePath(index))

    def is_file(self, index: QModelIndex) -> bool:
        return self.path(index).is_file()

    def is_dir(self, index: QModelIndex) -> bool:
        return self.path(index).is_dir()

    # ---------------------------------------------------------
    # Drag & Drop
    # ---------------------------------------------------------

    def flags(self, index):

        flags = super().flags(index)

        if not index.isValid():
            return flags

        return (
            flags
            | Qt.ItemIsDragEnabled
            | Qt.ItemIsDropEnabled
        )

    # ---------------------------------------------------------
    # Decoration
    # ---------------------------------------------------------

    def data(self, index, role=Qt.DisplayRole):

        if role == Qt.DecorationRole:

            path = self.path(index)

            if path.is_dir():
                return QIcon.fromTheme("folder")

            suffix = path.suffix.lower()

            if suffix == ".py":
                return QIcon.fromTheme("text-x-python")

            if suffix in {
                ".json",
                ".yaml",
                ".yml",
            }:
                return QIcon.fromTheme("text-x-script")

            if suffix in {
                ".md",
                ".txt",
            }:
                return QIcon.fromTheme("text-x-generic")

        return super().data(index, role)