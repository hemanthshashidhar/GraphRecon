from playwright.sync_api import Response

from graphrecon.browser.events import RESPONSE
from graphrecon.cache.response_cache import ResponseCache
from graphrecon.events.event_bus import EventBus
from graphrecon.models.response import ResponseModel
from graphrecon.utils.logger import logger


class ResponseCollector:
    """
    Collects browser responses and caches Playwright Response objects
    for analyzers.
    """

    def __init__(self, event_bus: EventBus) -> None:
        self._event_bus = event_bus

        self.responses: list[ResponseModel] = []

        self.cache = ResponseCache()

    def register(self) -> None:
        self._event_bus.subscribe(
            RESPONSE,
            self._on_response,
        )

    def _on_response(
        self,
        response: Response,
    ) -> None:

        # Keep the original Playwright response for analyzers
        self.cache.add(response)

        model = ResponseModel(
            url=response.url,
            status=response.status,
            status_text=response.status_text,
            resource_type=response.request.resource_type,
            headers=dict(response.headers),
            ok=response.ok,
        )

        self.responses.append(model)

        logger.info(
            "[RESPONSE] %s %s",
            model.status,
            model.url,
        )
