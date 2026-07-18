from ai_studio.providers.base import Provider


class AnthropicProvider(Provider):
    name = "anthropic"

    def chat(self, prompt: str) -> str:
        raise NotImplementedError