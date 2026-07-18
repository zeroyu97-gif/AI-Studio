from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QComboBox,
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class AIChat(QWidget):
    """
    AI Chat Panel
    """

    sendRequested = Signal(
        str,     # provider
        str,     # model
        float,   # temperature
        str,     # prompt
    )

    stopRequested = Signal()
    clearRequested = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # ---------------------------------
        # Toolbar
        # ---------------------------------

        toolbar = QHBoxLayout()

        toolbar.addWidget(QLabel("Provider"))

        self.provider = QComboBox()

        toolbar.addWidget(self.provider)

        toolbar.addWidget(QLabel("Model"))

        self.model = QComboBox()

        toolbar.addWidget(self.model)

        toolbar.addWidget(QLabel("Temp"))

        self.temperature = QDoubleSpinBox()

        self.temperature.setRange(0.0, 2.0)
        self.temperature.setSingleStep(0.1)
        self.temperature.setValue(0.7)

        toolbar.addWidget(self.temperature)

        layout.addLayout(toolbar)

        # ---------------------------------
        # History
        # ---------------------------------

        self.history = QTextEdit()

        self.history.setReadOnly(True)

        layout.addWidget(self.history)

        # ---------------------------------
        # Prompt
        # ---------------------------------

        self.prompt = QTextEdit()

        self.prompt.setPlaceholderText(
            "Ask AI..."
        )

        self.prompt.setFixedHeight(120)

        layout.addWidget(self.prompt)

        # ---------------------------------
        # Buttons
        # ---------------------------------

        buttons = QHBoxLayout()

        self.send = QPushButton("Send")
        self.stop = QPushButton("Stop")
        self.clear = QPushButton("Clear")

        buttons.addStretch()

        buttons.addWidget(self.send)
        buttons.addWidget(self.stop)
        buttons.addWidget(self.clear)

        layout.addLayout(buttons)

        # ---------------------------------

        self.send.clicked.connect(
            self._send
        )

        self.stop.clicked.connect(
            self.stopRequested.emit
        )

        self.clear.clicked.connect(
            self._clear
        )

    # ---------------------------------------------------------

    def _send(self):

        prompt = self.prompt.toPlainText().strip()

        if not prompt:
            return

        self.sendRequested.emit(
            self.provider.currentText(),
            self.model.currentText(),
            self.temperature.value(),
            prompt,
        )

        self.prompt.clear()

    # ---------------------------------------------------------

    def _clear(self):

        self.history.clear()

        self.clearRequested.emit()

    # ---------------------------------------------------------

    def append_user(self, text: str):

        self.history.append(
            f"<b>You:</b><br>{text}<br>"
        )

    def append_ai(self, text: str):

        self.history.append(
            f"<b>AI:</b><br>{text}<br>"
        )

    def append_system(self, text: str):

        self.history.append(
            f"<font color='gray'>{text}</font><br>"
        )

    # ---------------------------------------------------------

    def append_stream(self, text: str):

        cursor = self.history.textCursor()

        cursor.movePosition(cursor.End)

        cursor.insertText(text)

        self.history.setTextCursor(cursor)

    # ---------------------------------------------------------

    def set_models(
        self,
        models: list[str],
    ):

        self.model.clear()

        self.model.addItems(models)

    def set_providers(
        self,
        providers: list[str],
    ):

        self.provider.clear()

        self.provider.addItems(providers)

    # ---------------------------------------------------------

    def keyPressEvent(self, event):

        if (
            event.key() == Qt.Key_Return
            and event.modifiers() == Qt.ControlModifier
        ):

            self._send()
            return

        super().keyPressEvent(event)