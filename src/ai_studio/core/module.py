from typing import Protocol, runtime_checkable

@runtime_checkable
class Module(Protocol):

    def configure(self) -> None:
        ...

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...