from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Workspace:
    root: Path
    name: str

    @property
    def exists(self) -> bool:
        return self.root.exists()

    @property
    def src(self) -> Path:
        return self.root / "src"

    @property
    def git(self) -> Path:
        return self.root / ".git"