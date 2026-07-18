from __future__ import annotations

from PySide6.QtCore import QObject


class LSPController(QObject):

    def __init__(
        self,
        editor_area,
        lsp,
    ):
        super().__init__()

        self.editor_area = editor_area
        self.lsp = lsp

        editor_area.currentEditorChanged.connect(
            self.editor_changed
        )

        lsp.diagnosticsChanged.connect(
            self.update_diagnostics
        )

    def editor_changed(self, editor):

        if editor.path is None:
            return

        self.lsp.did_open(
            editor.path,
            editor.toPlainText(),
        )

        editor.textChanged.connect(
            lambda e=editor: self.document_changed(e)
        )

    def document_changed(self, editor):

        self.lsp.did_change(
            editor.path,
            editor.document().revision(),
            editor.toPlainText(),
        )

    def update_diagnostics(self, path):

        editor = self.editor_area.find_editor(path)

        if editor is None:
            return

        editor.update_diagnostics(
            self.lsp.diagnostics(path)
        )