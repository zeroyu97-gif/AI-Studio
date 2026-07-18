class AIStudioError(Exception):
    """Base project exception."""


class ContainerError(AIStudioError):
    """Base container error."""


class ServiceNotFoundError(ContainerError):
    pass


class ServiceAlreadyRegisteredError(ContainerError):
    pass