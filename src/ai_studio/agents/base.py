from abc import ABC, abstractmethod

from .context import AgentContext
from .task import AgentTask


class Agent(ABC):

    name: str

    @abstractmethod
    def execute(
        self,
        task: AgentTask,
        context: AgentContext,
    ) -> str:
        ...