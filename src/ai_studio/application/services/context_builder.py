from dataclasses import dataclass


@dataclass(slots=True)
class ChatContext:
    workspace: str | None
    active_file: str | None
    selection: str | None
    history: list[str]


class ContextBuilder:

    @staticmethod
    def build(
        workspace,
        active_file,
        selection,
        history,
    ) -> ChatContext:

        return ChatContext(
            workspace=workspace,
            active_file=active_file,
            selection=selection,
            history=history,
        )