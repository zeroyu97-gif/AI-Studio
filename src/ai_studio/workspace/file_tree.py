from collections.abc import Iterator
from pathlib import Path


class FileTree:
    def __init__(self, root: Path) -> None:
        self.root = root

    def files(self) -> Iterator[Path]:
        return (p for p in self.root.rglob("*") if p.is_file())