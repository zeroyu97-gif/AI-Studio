from __future__ import annotations

import re

from PySide6.QtGui import (
    QColor,
    QTextCharFormat,
    QFont,
    QSyntaxHighlighter,
)


class PythonHighlighter(QSyntaxHighlighter):

    def __init__(self, document):
        super().__init__(document)

        self.rules = []

        def fmt(color, bold=False, italic=False):
            f = QTextCharFormat()
            f.setForeground(QColor(color))

            if bold:
                f.setFontWeight(QFont.Bold)

            f.setFontItalic(italic)

            return f

        keyword = fmt("#4FC3F7", True)
        string = fmt("#A5D6A7")
        comment = fmt("#757575", italic=True)
        number = fmt("#FFB74D")
        function = fmt("#81C784")
        klass = fmt("#64B5F6", True)
        decorator = fmt("#BA68C8")
        builtin = fmt("#FFD54F")
        operator = fmt("#E57373")

        keywords = [
            "False", "None", "True",
            "and", "as", "assert",
            "async", "await",
            "break",
            "class",
            "continue",
            "def",
            "del",
            "elif",
            "else",
            "except",
            "finally",
            "for",
            "from",
            "global",
            "if",
            "import",
            "in",
            "is",
            "lambda",
            "match",
            "case",
            "nonlocal",
            "not",
            "or",
            "pass",
            "raise",
            "return",
            "try",
            "while",
            "with",
            "yield",
        ]

        builtins = [
            "print",
            "len",
            "range",
            "list",
            "dict",
            "set",
            "tuple",
            "str",
            "int",
            "float",
            "bool",
            "type",
            "isinstance",
            "enumerate",
            "zip",
            "map",
            "filter",
            "sum",
            "min",
            "max",
        ]

        for word in keywords:
            self.rules.append(
                (
                    re.compile(rf"\b{word}\b"),
                    keyword,
                )
            )

        for word in builtins:
            self.rules.append(
                (
                    re.compile(rf"\b{word}\b"),
                    builtin,
                )
            )

        self.rules.extend(
            [
                (
                    re.compile(r"\b\d+(\.\d+)?\b"),
                    number,
                ),
                (
                    re.compile(r"'[^']*'"),
                    string,
                ),
                (
                    re.compile(r'"[^"]*"'),
                    string,
                ),
                (
                    re.compile(r"#.*"),
                    comment,
                ),
                (
                    re.compile(r"@\w+"),
                    decorator,
                ),
                (
                    re.compile(r"\bclass\s+(\w+)"),
                    klass,
                ),
                (
                    re.compile(r"\bdef\s+(\w+)"),
                    function,
                ),
                (
                    re.compile(
                        r"==|!=|<=|>=|=|\+|-|\*|/|//|%|\*\*"
                    ),
                    operator,
                ),
            ]
        )

    def highlightBlock(self, text: str):

        for pattern, style in self.rules:

            for match in pattern.finditer(text):

                if pattern.pattern.startswith(r"\bclass"):

                    start = match.start(1)
                    length = len(match.group(1))

                elif pattern.pattern.startswith(r"\bdef"):

                    start = match.start(1)
                    length = len(match.group(1))

                else:

                    start = match.start()
                    length = match.end() - start

                self.setFormat(
                    start,
                    length,
                    style,
                )