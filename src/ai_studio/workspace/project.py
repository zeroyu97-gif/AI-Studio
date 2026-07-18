from pathlib import Path


class Project:
    def __init__(self, path: Path) -> None:
        self.path = path

    @property
    def name(self) -> str:
        return self.path.name

    @property
    def root(self) -> Path:
        return self.path

    @property
    def exists(self) -> bool:
        return self.path.exists()