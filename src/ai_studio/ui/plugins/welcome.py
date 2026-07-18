from __future__ import annotations

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class WelcomePlugin:

    name = "welcome"

    def setup(self, window):

        label = QLabel(
            "Welcome to AI Studio"
        )

        label.setAlignment(Qt.AlignCenter)

        window.editor.addTab(
            label,
            "Welcome",
        )