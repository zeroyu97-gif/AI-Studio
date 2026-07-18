from .anthropic.provider import AnthropicProvider
from .gemini.provider import GeminiProvider
from .ollama.provider import OllamaProvider
from .openai.provider import OpenAIProvider

from .manager import ProviderManager


def register_builtin(manager: ProviderManager) -> None:
    manager.register(OpenAIProvider())
    manager.register(OllamaProvider())
    manager.register(GeminiProvider())
    manager.register(AnthropicProvider())