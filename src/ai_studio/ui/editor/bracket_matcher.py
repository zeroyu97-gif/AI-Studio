from __future__ import annotations

from PySide6.QtGui import QTextCursor


class BracketMatcher:

    PAIRS = {
        "(": ")",
        "[": "]",
        "{": "}",
        ")": "(",
        "]": "[",
        "}": "{",
    }

    OPEN = "([{"
    CLOSE = ")]}"

    def find_match(self, document, position: int):

        if position < 0:
            return None

        text = document.toPlainText()

        if not text:
            return None

        if position >= len(text):
            position = len(text) - 1

        ch = text[position]

        if ch in self.OPEN:
            return self._forward(text, position)

        if ch in self.CLOSE:
            return self._backward(text, position)

        return None

    def _forward(self, text, start):

        opening = text[start]
        closing = self.PAIRS[opening]

        depth = 0

        for i in range(start, len(text)):

            c = text[i]

            if c == opening:
                depth += 1

            elif c == closing:

                depth -= 1

                if depth == 0:
                    return start, i

        return None

    def _backward(self, text, start):

        closing = text[start]
        opening = self.PAIRS[closing]

        depth = 0

        for i in range(start, -1, -1):

            c = text[i]

            if c == closing:
                depth += 1

            elif c == opening:

                depth -= 1

                if depth == 0:
                    return i, start

        return None