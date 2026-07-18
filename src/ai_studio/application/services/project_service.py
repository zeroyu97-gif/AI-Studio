class ProjectService:

    def open(self, path: str) -> None:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError

    def current(self) -> str | None:
        raise NotImplementedError