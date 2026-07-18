from __future__ import annotations

from .service_container import ServiceContainer


_container: ServiceContainer | None = None


def set_container(container: ServiceContainer):

    global _container

    _container = container


def get(service_type):

    if _container is None:
        raise RuntimeError(
            "ServiceContainer is not initialized."
        )

    return _container.resolve(service_type)