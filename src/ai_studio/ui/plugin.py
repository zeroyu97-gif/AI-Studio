from __future__ import annotations

from typing import Protocol

from PySide6.QtWidgets import QMainWindow


class UIPlugin(Protocol):

    name: str

    def setup(
        self,
        window: QMainWindow,
    ) -> None:
        ...