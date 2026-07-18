import logging

from ai_studio.plugins.base import Plugin

logger = logging.getLogger(__name__)


class SystemPlugin(Plugin):

    name = "system"
    version = "0.1.0"

    def load(self) -> None:
        logger.info("System plugin loaded")

    def unload(self) -> None:
        logger.info("System plugin unloaded")