from ai_studio.providers.base import Provider


class OllamaProvider(Provider):
    name = "ollama"

    def chat(self, prompt: str) -> str:
        raise NotImplementedError