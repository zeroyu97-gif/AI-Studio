from pathlib import Path
from PySide6.QtCore import QObject, Signal

class EditorViewModel(QObject):

    opened = Signal(Path)
    saved = Signal(Path)

    def open(self, path: Path):
        self.opened.emit(path)

    def save(self, path: Path):
        self.saved.emit(path)