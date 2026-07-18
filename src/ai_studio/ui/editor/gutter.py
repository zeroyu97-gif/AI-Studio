from __future__ import annotations

from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QWidget


class Gutter(QWidget):
    """
    VS Code style editor gutter.
    """

    def __init__(self, editor):
        super().__init__(editor)

        self.editor = editor

        self.breakpoints = set()
        self.bookmarks = set()

    # -----------------------------------------------------

    def sizeHint(self):

        return QSize(
            self.editor.gutter_width(),
            0,
        )

    # -----------------------------------------------------

    def paintEvent(self, event):

        self.editor.paint_gutter(event)

    # -----------------------------------------------------

    def mousePressEvent(self, event):

        if event.button() != Qt.LeftButton:
            return

        block = self.editor.firstVisibleBlock()

        number = block.blockNumber()

        top = round(
            self.editor.blockBoundingGeometry(block)
            .translated(self.editor.contentOffset())
            .top()
        )

        bottom = top + round(
            self.editor.blockBoundingRect(block).height()
        )

        while block.isValid():

            if top <= event.position().y() <= bottom:

                if number in self.breakpoints:
                    self.breakpoints.remove(number)
                else:
                    self.breakpoints.add(number)

                self.update()

                return

            block = block.next()

            top = bottom

            bottom = top + round(
                self.editor.blockBoundingRect(block).height()
            )

            number += 1