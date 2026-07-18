from __future__ import annotations

from core.bus.command_bus import CommandBus
from core.bus.event_bus import EventBus

from workspace.workspace_manager import WorkspaceManager

from .service_container import ServiceContainer


class ApplicationContext:

    def __init__(self):

        self.services = ServiceContainer()

        self._register_core()

    def _register_core(self):

        self.services.register(
            CommandBus,
            CommandBus(),
        )

        self.services.register(
            EventBus,
            EventBus(),
        )

        self.services.register(
            WorkspaceManager,
            WorkspaceManager(),
        )