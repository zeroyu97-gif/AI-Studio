from dataclasses import dataclass

from core.bus.command import Command


@dataclass(slots=True)
class SaveFile(Command):
    pass