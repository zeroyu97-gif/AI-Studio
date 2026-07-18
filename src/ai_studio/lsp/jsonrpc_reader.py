from __future__ import annotations

import json


class JsonRpcReader:

    def __init__(self):
        self.buffer = bytearray()

    def feed(self, data: bytes):

        self.buffer.extend(data)

        messages = []

        while True:

            header_end = self.buffer.find(b"\r\n\r\n")

            if header_end == -1:
                break

            header = self.buffer[:header_end].decode()

            length = None

            for line in header.split("\r\n"):

                if line.lower().startswith("content-length"):

                    length = int(
                        line.split(":")[1].strip()
                    )

            if length is None:
                break

            start = header_end + 4

            end = start + length

            if len(self.buffer) < end:
                break

            payload = bytes(
                self.buffer[start:end]
            )

            del self.buffer[:end]

            messages.append(
                json.loads(payload.decode())
            )

        return messages