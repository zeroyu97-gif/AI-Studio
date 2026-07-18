class BuildUseCase:
    """Run project build."""

    def __init__(self, build_service) -> None:
        self._build_service = build_service

    def execute(self):
        return self._build_service.build()