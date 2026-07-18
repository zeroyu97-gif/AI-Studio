from PySide6.QtCore import QObject


class WorkspaceController(QObject):

    def __init__(
        self,
        workspace,
        explorer,
        editor,
    ):
        super().__init__()

        self.workspace = workspace
        self.explorer = explorer
        self.editor = editor

        workspace.workspaceOpened.connect(
            self.workspace_opened
        )

    def workspace_opened(self, ws):

        self.explorer.set_root(
            ws.root
        )