from __future__ import annotations

from dataclasses import dataclass

from PySide6.QtGui import QTextBlock


@dataclass(slots=True)
class FoldRegion:

    start_block: int
    end_block: int
    level: int
    collapsed: bool = False


class FoldingManager:

    def __init__(self, editor):

        self.editor = editor

        self.regions: list[FoldRegion] = []

    # ---------------------------------------------------------

    def rebuild(self):

        self.regions.clear()

        document = self.editor.document()

        stack: list[tuple[int, int]] = []

        block = document.firstBlock()

        while block.isValid():

            line = block.text()

            indent = self._indent(line)

            number = block.blockNumber()

            while stack and indent <= stack[-1][1]:

                start, level = stack.pop()

                if number - start > 1:

                    self.regions.append(

                        FoldRegion(

                            start_block=start,

                            end_block=number - 1,

                            level=level,

                        )

                    )

            if line.strip():

                stack.append((number, indent))

            block = block.next()

        last = document.blockCount() - 1

        while stack:

            start, level = stack.pop()

            if last - start > 0:

                self.regions.append(

                    FoldRegion(

                        start_block=start,

                        end_block=last,

                        level=level,

                    )

                )

    # ---------------------------------------------------------

    @staticmethod
    def _indent(text: str):

        indent = 0

        for ch in text:

            if ch == " ":
                indent += 1

            elif ch == "\t":
                indent += 4

            else:
                break

        return indent

    # ---------------------------------------------------------

    def region_for_block(self, block_number):

        for region in self.regions:

            if region.start_block == block_number:
                return region

        return None