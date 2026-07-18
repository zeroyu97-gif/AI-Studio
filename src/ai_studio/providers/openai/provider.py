from ai_studio.providers.base import Provider


class OpenAIProvider(Provider):

    name = "openai"

    def chat(self, prompt: str) -> str:

        return "Not implemented"