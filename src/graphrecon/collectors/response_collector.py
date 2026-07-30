from playwright.sync_api import Response

from graphrecon.cache.response_cache import ResponseCache
from graphrecon.events.event_bus import EventBus
from graphrecon.models.response import ResponseModel
from graphrecon.browser.events import RESPONSE
from graphrecon.utils.logger import logger


class ResponseCollector:

    def __init__(self, event_bus: EventBus):

        self.event_bus = event_bus

        self.responses: list[ResponseModel] = []

        self.cache = ResponseCache()

    def register(self) -> None:

        self.event_bus.subscribe(
            RESPONSE,
            self.handle_response,
        )

    def handle_response(
        self,
        response: Response,
    ) -> None:

        self.cache.add(response)

        self.responses.append(
            ResponseModel(
                url=response.url,
                status=response.status,
            )
        )

        logger.info(
            "[RESPONSE] %s %s",
            response.status,
            response.url,
        )
