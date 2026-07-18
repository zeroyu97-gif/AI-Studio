from __future__ import annotations

import json


class JsonRpcWriter:

    @staticmethod
    def encode(message: dict) -> bytes:

        payload = json.dumps(
            message,
            separators=(",", ":"),
        ).encode("utf-8")

        header = (
            f"Content-Length: {len(payload)}\r\n\r\n"
        ).encode("ascii")

        return header + payload