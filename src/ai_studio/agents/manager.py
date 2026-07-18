from .base import Agent


class AgentManager:

    def __init__(self) -> None:
        self._agents: dict[str, Agent] = {}

    def register(self, agent: Agent) -> None:
        self._agents[agent.name] = agent

    def get(self, name: str) -> Agent:
        return self._agents[name]

    def available(self) -> tuple[str, ...]:
        return tuple(self._agents.keys())