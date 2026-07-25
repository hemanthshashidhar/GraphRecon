from playwright.sync_api import ConsoleMessage, Page, Request, Response

from graphrecon.browser.events import (
    CONSOLE,
    PAGE_ERROR,
    REQUEST,
    RESPONSE,
)
from graphrecon.events.event_bus import EventBus
from graphrecon.models.page import PageModel
from graphrecon.utils.logger import logger


class PageCollector:
    """
    Collects information about visited pages.
    """

    def __init__(self, event_bus: EventBus) -> None:
        self._event_bus = event_bus

        self.pages: list[PageModel] = []

    def register(self) -> None:
        self._event_bus.subscribe(REQUEST, self._on_request)
        self._event_bus.subscribe(RESPONSE, self._on_response)
        self._event_bus.subscribe(CONSOLE, self._on_console)
        self._event_bus.subscribe(PAGE_ERROR, self._on_page_error)

    def collect_page(self, page: Page) -> None:
        """
        Capture metadata about the current page.
        """

        model = PageModel(
            url=page.url,
            final_url=page.url,
            title=page.title(),
        )

        self.pages.append(model)

        logger.info("[PAGE] %s", model.title)

    def _on_request(self, request: Request) -> None:
        logger.info("[REQUEST] %s %s", request.method, request.url)

    def _on_response(self, response: Response) -> None:
        logger.info("[RESPONSE] %s %s", response.status, response.url)

    def _on_console(self, message: ConsoleMessage) -> None:
        logger.info("[CONSOLE] %s", message.text)

    def _on_page_error(self, error: Exception) -> None:
        logger.error("[PAGE ERROR] %s", error)
