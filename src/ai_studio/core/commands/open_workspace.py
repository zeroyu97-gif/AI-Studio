from dataclasses import dataclass
from pathlib import Path

from core.bus.command import Command


@dataclass(slots=True)
class OpenWorkspace(Command):

    path: Path