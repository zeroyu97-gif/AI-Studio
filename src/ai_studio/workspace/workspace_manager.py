from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QObject, Signal

from .workspace import Workspace


class WorkspaceManager(QObject):

    workspaceOpened = Signal(Workspace)
    workspaceClosed = Signal()
    workspaceChanged = Signal()

    def __init__(self):
        super().__init__()

        self._workspace: Workspace | None = None

    @property
    def workspace(self):
        return self._workspace

    def open(self, folder: Path):

        folder = folder.resolve()

        self._workspace = Workspace(
            root=folder,
            name=folder.name,
        )

        self.workspaceOpened.emit(
            self._workspace
        )

    def close(self):

        self._workspace = None

        self.workspaceClosed.emit()

    def is_open(self):

        return self._workspace is not None