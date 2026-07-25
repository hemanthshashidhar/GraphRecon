from playwright.sync_api import Request

from graphrecon.browser.events import REQUEST
from graphrecon.events.event_bus import EventBus
from graphrecon.models.request import RequestModel
from graphrecon.utils.logger import logger


class RequestCollector:
    """
    Collects all browser requests.
    """

    def __init__(self, event_bus: EventBus) -> None:
        self._event_bus = event_bus
        self.requests: list[RequestModel] = []

    def register(self) -> None:
        self._event_bus.subscribe(
            REQUEST,
            self._on_request,
        )

    def _on_request(self, request: Request) -> None:

        model = RequestModel(
            method=request.method,
            url=request.url,
            resource_type=request.resource_type,
            is_navigation=request.is_navigation_request(),
            headers=dict(request.headers),
        )

        self.requests.append(model)

        logger.info(
            "[REQUEST] %s %s (%s)",
            model.method,
            model.url,
            model.resource_type,
        )
