from __future__ import annotations

from .module import Module


class ModuleManager:

    def __init__(self) -> None:
        self._modules: list[Module] = []

    def register(self, module: Module) -> None:
        self._modules.append(module)

    def configure(self) -> None:
        for module in self._modules:
            module.configure()

    def start(self) -> None:
        for module in self._modules:
            module.start()

    def stop(self) -> None:
        for module in reversed(self._modules):
            module.stop()