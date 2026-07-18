from pathlib import Path

from .project import Project
from .workspace import Workspace


class WorkspaceManager:
    """Manage the current workspace and project."""

    def __init__(self) -> None:
        self.workspace: Workspace | None = None
        self.project: Project | None = None

    def open(self, root: Path) -> Project:
        self.workspace = Workspace(root)
        self.project = Project(root)
        return self.project

    def close(self) -> None:
        self.workspace = None
        self.project = None

    def save(self) -> None:
        """Persist workspace state."""
        # TODO: implement session persistence
        pass