from ai_studio.application.dto.chat_request import ChatRequest
from ai_studio.application.dto.chat_response import ChatResponse


class ChatUseCase:
    """Send a message to the AI provider."""

    def __init__(self, chat_service) -> None:
        self._chat_service = chat_service

    def execute(self, request: ChatRequest) -> ChatResponse:
        return self._chat_service.chat(request)