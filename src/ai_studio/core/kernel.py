from __future__ import annotations

from ai_studio.config import logger

from .container import ServiceContainer
from .event_bus import EventBus
from .manager import ModuleManager


class Kernel:
    """Application kernel."""

    def __init__(self) -> None:
        self.container = ServiceContainer()
        self.events = EventBus()
        self.modules = ModuleManager()

    def boot(self) -> None:
        logger.info("Kernel booting...")

        self.modules.configure()
        self.modules.start()

        logger.success("Kernel ready.")

    def shutdown(self) -> None:
        logger.info("Kernel shutting down...")

        self.modules.stop()

        logger.success("Kernel stopped.")