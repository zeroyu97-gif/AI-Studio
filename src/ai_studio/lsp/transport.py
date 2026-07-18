from __future__ import annotations

import json

from PySide6.QtCore import QObject, QProcess, Signal


class LSPTransport(QObject):

    messageReceived = Signal(dict)

    def __init__(self):
        super().__init__()

        self.process = QProcess()

        self.process.readyReadStandardOutput.connect(
            self._read
        )

    def start(
        self,
        program,
        arguments,
    ):

        self.process.start(
            program,
            arguments,
        )

    def send(self, message):

        payload = json.dumps(message)

        header = (
            f"Content-Length: {len(payload.encode())}\r\n\r\n"
        )

        self.process.write(
            header.encode()
        )

        self.process.write(
            payload.encode()
        )

    def _read(self):

        data = bytes(
            self.process.readAllStandardOutput()
        )

        # Следующий этап:
        # полноценный JSON-RPC parser