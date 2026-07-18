from __future__ import annotations


class ServiceContainer:

    def __init__(self):
        self._services = {}

    def register(self, service_type, instance):

        self._services[service_type] = instance

    def resolve(self, service_type):

        if service_type not in self._services:
            raise KeyError(
                f"Service '{service_type.__name__}' not registered."
            )

        return self._services[service_type]

    def contains(self, service_type):

        return service_type in self._services