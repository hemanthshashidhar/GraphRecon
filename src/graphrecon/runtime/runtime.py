from playwright.sync_api import ConsoleMessage, Request, Response

from graphrecon.browser.browser_manager import BrowserManager
from graphrecon.browser.events import (
    CONSOLE,
    PAGE_ERROR,
    REQUEST,
    RESPONSE,
)
from graphrecon.events.event_bus import EventBus
from graphrecon.utils.logger import logger


class Runtime:
    """
    Coordinates GraphRecon runtime.
    """

    def __init__(self) -> None:
        self.event_bus = EventBus()
        self.browser = BrowserManager(self.event_bus)

        self._register_events()

    def _register_events(self) -> None:
        self.event_bus.subscribe(REQUEST, self._request)

        self.event_bus.subscribe(RESPONSE, self._response)

        self.event_bus.subscribe(CONSOLE, self._console)

        self.event_bus.subscribe(PAGE_ERROR, self._page_error)

    def _request(self, request: Request) -> None:
        logger.info("[REQUEST] %s %s", request.method, request.url)

    def _response(self, response: Response) -> None:
        logger.info("[RESPONSE] %s %s", response.status, response.url)

    def _console(self, message: ConsoleMessage) -> None:
        logger.info("[CONSOLE] %s", message.text)

    def _page_error(self, error: Exception) -> None:
        logger.error("[PAGE ERROR] %s", error)

    def scan(self, url: str) -> None:
        self.browser.start()

        try:
            self.browser.open(url)

        finally:
            self.browser.stop()
