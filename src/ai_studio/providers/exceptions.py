class ProviderError(Exception):
    """Base provider error."""


class ProviderNotFoundError(ProviderError):
    pass


class ProviderAlreadyRegisteredError(ProviderError):
    pass