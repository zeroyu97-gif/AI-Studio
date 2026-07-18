from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter


class IndentGuides:

    def __init__(self, editor):

        self.editor = editor

        self.color = QColor("#404040")

    def paint(self, painter: QPainter):

        block = self.editor.firstVisibleBlock()

        offset = self.editor.contentOffset()

        tab_width = self.editor.fontMetrics().horizontalAdvance(" ")

        indent_width = tab_width * 4

        while block.isValid():

            if block.isVisible():

                rect = self.editor.blockBoundingGeometry(
                    block
                ).translated(offset)

                top = int(rect.top())
                bottom = int(rect.bottom())

                text = block.text()

                indent = 0

                for ch in text:

                    if ch == " ":
                        indent += 1

                    elif ch == "\t":
                        indent += 4

                    else:
                        break

                levels = indent // 4

                painter.setPen(self.color)

                for level in range(levels):

                    x = (
                        self.editor.gutter_width()
                        + level * indent_width
                        + indent_width // 2
                    )

                    painter.drawLine(
                        x,
                        top,
                        x,
                        bottom,
                    )

            block = block.next()