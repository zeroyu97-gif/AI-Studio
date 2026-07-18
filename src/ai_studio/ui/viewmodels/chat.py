from PySide6.QtCore import QObject, Signal

class ChatViewModel(QObject):

    responseReady = Signal(str)

    def __init__(self, providers):
        super().__init__()

        self.providers = providers

    def ask(
        self,
        provider,
        prompt,
    ):

        result = self.providers.get(provider).chat(prompt)

        self.responseReady.emit(result.text)