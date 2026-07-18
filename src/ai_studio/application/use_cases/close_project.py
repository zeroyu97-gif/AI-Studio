from ai_studio.workspace.manager import WorkspaceManager


class CloseProjectUseCase:
    """Close the current workspace."""

    def __init__(self, workspace_manager: WorkspaceManager) -> None:
        self._workspace_manager = workspace_manager

    def execute(self) -> None:
        self._workspace_manager.close()