from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QObject, Signal

from .client import LSPClient


class LSPManager(QObject):

    diagnosticsChanged = Signal(Path)
    completionReady = Signal(list)

    def __init__(self):
        super().__init__()

        self.client = LSPClient()

        self.client.diagnostics.connect(
            self.diagnosticsChanged
        )

        self.client.completion.connect(
            self.completionReady
        )

    def start(self):

        self.client.start()

    def stop(self):

        self.client.stop()