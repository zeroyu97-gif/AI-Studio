from ai_studio.providers.base import Provider


class GeminiProvider(Provider):
    name = "gemini"

    def chat(self, prompt: str) -> str:
        raise NotImplementedError