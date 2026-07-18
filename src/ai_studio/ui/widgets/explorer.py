from __future__ import annotations

import shutil
from pathlib import Path

from PySide6.QtCore import QFileSystemWatcher, Qt, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QInputDialog,
    QMenu,
    QMessageBox,
    QTreeView,
)

from .explorer_model import ExplorerModel


class Explorer(QTreeView):
    """
    Project Explorer
    """

    fileOpenRequested = Signal(Path)
    rootChanged = Signal(Path)
    fileDeleted = Signal(Path)
    fileRenamed = Signal(Path, Path)
    fileCreated = Signal(Path)
    folderCreated = Signal(Path)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._root: Path | None = None

        self._model = ExplorerModel(self)
        self.setModel(self._model)

        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)

        self.setAnimated(True)
        self.setSortingEnabled(True)
        self.sortByColumn(0, Qt.AscendingOrder)

        self.setAlternatingRowColors(True)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(self.InternalMove)

        self.setContextMenuPolicy(Qt.CustomContextMenu)

        self.doubleClicked.connect(self._double_clicked)
        self.customContextMenuRequested.connect(
            self._context_menu
        )

        self.watcher = QFileSystemWatcher(self)

        self.watcher.directoryChanged.connect(
            lambda _: self.refresh()
        )

        self.watcher.fileChanged.connect(
            lambda _: self.refresh()
        )

    # ----------------------------------------------------

    @property
    def root_path(self):
        return self._root

    def set_root(self, path: Path):

        path = path.resolve()

        self._root = path

        index = self._model.setRootPath(str(path))

        self.setRootIndex(index)

        self.watcher.removePaths(
            self.watcher.directories()
        )

        self.watcher.addPath(str(path))

        self.expandToDepth(0)

        self.rootChanged.emit(path)

    # ----------------------------------------------------

    def current_path(self):

        index = self.currentIndex()

        if not index.isValid():
            return None

        return self._model.path(index)

    # ----------------------------------------------------

    def refresh(self):

        if self._root is None:
            return

        index = self._model.setRootPath("")

        index = self._model.setRootPath(
            str(self._root)
        )

        self.setRootIndex(index)

    # ----------------------------------------------------

    def _double_clicked(self, index):

        path = self._model.path(index)

        if path.is_file():

            self.fileOpenRequested.emit(path)

    # ----------------------------------------------------

    def create_file(self):

        parent = self.current_path()

        if parent is None:
            return

        if parent.is_file():
            parent = parent.parent

        name, ok = QInputDialog.getText(
            self,
            "New File",
            "File name:",
            text="new_file.py",
        )

        if not ok or not name:
            return

        path = parent / name

        path.touch()

        self.refresh()

        self.fileCreated.emit(path)

    # ----------------------------------------------------

    def create_folder(self):

        parent = self.current_path()

        if parent is None:
            return

        if parent.is_file():
            parent = parent.parent

        name, ok = QInputDialog.getText(
            self,
            "New Folder",
            "Folder name:",
            text="New Folder",
        )

        if not ok or not name:
            return

        folder = parent / name

        folder.mkdir(exist_ok=True)

        self.refresh()

        self.folderCreated.emit(folder)

    # ----------------------------------------------------

    def rename(self, path: Path):

        name, ok = QInputDialog.getText(
            self,
            "Rename",
            "New name:",
            text=path.name,
        )

        if not ok or not name:
            return

        new = path.parent / name

        path.rename(new)

        self.refresh()

        self.fileRenamed.emit(path, new)

    # ----------------------------------------------------

    def delete(self, path: Path):

        answer = QMessageBox.question(
            self,
            "Delete",
            f"Delete\n{path.name} ?",
        )

        if answer != QMessageBox.Yes:
            return

        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()

        self.refresh()

        self.fileDeleted.emit(path)

    # ----------------------------------------------------

    def _context_menu(self, pos):

        index = self.indexAt(pos)

        if not index.isValid():
            return

        path = self._model.path(index)

        menu = QMenu(self)

        open_action = QAction("Open", self)
        new_file = QAction("New File", self)
        new_folder = QAction("New Folder", self)
        rename = QAction("Rename", self)
        delete = QAction("Delete", self)
        refresh = QAction("Refresh", self)

        menu.addAction(open_action)

        menu.addSeparator()

        menu.addAction(new_file)
        menu.addAction(new_folder)

        menu.addSeparator()

        menu.addAction(rename)
        menu.addAction(delete)

        menu.addSeparator()

        menu.addAction(refresh)

        open_action.triggered.connect(
            lambda: self.fileOpenRequested.emit(path)
        )

        new_file.triggered.connect(
            self.create_file
        )

        new_folder.triggered.connect(
            self.create_folder
        )

        rename.triggered.connect(
            lambda: self.rename(path)
        )

        delete.triggered.connect(
            lambda: self.delete(path)
        )

        refresh.triggered.connect(
            self.refresh
        )

        menu.exec(
            self.viewport().mapToGlobal(pos)
        )