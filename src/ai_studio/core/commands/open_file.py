from dataclasses import dataclass
from pathlib import Path

from core.bus.command import Command


@dataclass(slots=True)
class OpenFile(Command):

    path: Path