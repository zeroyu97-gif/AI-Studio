from pathlib import Path

from PySide6.QtWidgets import QVBoxLayout, QWidget

from .editor import Editor


class EditorTab(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.editor = Editor()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.editor)

    def load(self, path: Path) -> None:
        self.editor.load_file(path)