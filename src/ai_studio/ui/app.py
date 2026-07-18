from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from .main_window import MainWindow


class StudioApplication(QApplication):
    """Main Qt application."""

    def __init__(self, argv: list[str]) -> None:
        super().__init__(argv)

        self.setApplicationName("AI Studio")
        self.setOrganizationName("AI Studio")
        self.setApplicationVersion("0.1.0")

        self.window = MainWindow()

    def run(self) -> int:
        self.window.show()
        return self.exec()


def main() -> int:
    app = StudioApplication(sys.argv)
    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())