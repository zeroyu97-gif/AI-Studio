"""
Application bootstrap module.

Handles initialization of the AI Studio application, including
directory setup and startup messaging.
"""

from __future__ import annotations

from pathlib import Path


class Bootstrap:
    """
    Application bootstrap handler.

    Manages initialization of the AI Studio application including
    workspace directory creation and startup procedures.
    """

    def __init__(self) -> None:
        """Initialize bootstrap with current working directory."""
        self.root = Path.cwd()

    def prepare(self) -> None:
        """
        Create necessary application directories.

        Creates the following directories if they don't exist:
        - logs: For application logs
        - cache: For cached data
        - workspace: For project workspaces
        - plugins: For plugin storage
        - settings: For application settings
        """
        directories = (
            "logs",
            "cache",
            "workspace",
            "plugins",
            "settings",
        )

        for directory in directories:
            (self.root / directory).mkdir(
                exist_ok=True,
                parents=True,
            )

    def start(self) -> None:
        """
        Start the application.

        Performs initialization steps and displays startup information.
        """
        self.prepare()

        print()
        print("========================================")
        print("🦔 AI Studio")
        print("Version:", __import__("ai_studio").__version__)
        print("AI Manager: Ёжик")
        print("Status: READY")
        print("========================================")
        print()


def bootstrap() -> None:
    """
    Bootstrap the AI Studio application.

    Entry point for application initialization.
    """
    Bootstrap().start()
