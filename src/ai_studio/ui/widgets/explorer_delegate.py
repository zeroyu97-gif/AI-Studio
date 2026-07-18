from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import (
    QApplication,
    QFileIconProvider,
    QStyledItemDelegate,
)


class ExplorerDelegate(QStyledItemDelegate):
    """
    VS Code style delegate.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.icons = QFileIconProvider()

        self.git_state: dict[Path, str] = {}
        self.diagnostics: dict[Path, int] = {}

    # -------------------------------------------------

    def set_git_state(
        self,
        state: dict[Path, str],
    ):
        self.git_state = state

    def set_diagnostics(
        self,
        diagnostics: dict[Path, int],
    ):
        self.diagnostics = diagnostics

    # -------------------------------------------------

    def paint(
        self,
        painter: QPainter,
        option,
        index,
    ):

        super().paint(
            painter,
            option,
            index,
        )

        model = index.model()

        path = model.path(index)

        rect = QRect(option.rect)

        x = rect.right() - 18

        # ------------------------------
        # Git decoration
        # ------------------------------

        if path in self.git_state:

            state = self.git_state[path]

            color = QColor()

            if state == "modified":
                color = QColor("#ff9800")

            elif state == "added":
                color = QColor("#4caf50")

            elif state == "deleted":
                color = QColor("#f44336")

            elif state == "ignored":
                color = QColor("#757575")

            painter.save()

            painter.setBrush(color)

            painter.setPen(Qt.NoPen)

            painter.drawEllipse(
                x,
                rect.center().y() - 4,
                8,
                8,
            )

            painter.restore()

        # ------------------------------
        # LSP diagnostics
        # ------------------------------

        if path in self.diagnostics:

            severity = self.diagnostics[path]

            painter.save()

            if severity == 1:

                painter.setBrush(
                    QColor("#f44336")
                )

            else:

                painter.setBrush(
                    QColor("#ff9800")
                )

            painter.setPen(Qt.NoPen)

            painter.drawRect(
                x - 14,
                rect.center().y() - 4,
                8,
                8,
            )

            painter.restore()