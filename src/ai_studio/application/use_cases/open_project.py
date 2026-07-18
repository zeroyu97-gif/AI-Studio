from ai_studio.workspace.manager import WorkspaceManager


class OpenProjectUseCase:
    """Open a workspace/project."""

    def __init__(self, workspace_manager: WorkspaceManager) -> None:
        self._workspace_manager = workspace_manager

    def execute(self, path: str):
        return self._workspace_manager.open(path)