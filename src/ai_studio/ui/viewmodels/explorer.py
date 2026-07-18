from pathlib import Path
from PySide6.QtCore import QObject, Signal

class ExplorerViewModel(QObject):

    fileOpened = Signal(Path)

    def __init__(self, workspace):
        super().__init__()
        self.workspace = workspace

    def open_project(self, path: Path):
        self.workspace.open(path)

    def open_file(self, path: Path):
        self.fileOpened.emit(path)