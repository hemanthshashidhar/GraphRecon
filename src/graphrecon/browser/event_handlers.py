from playwright.sync_api import ConsoleMessage, Page, Request, Response

from graphrecon.browser.events import (
    CONSOLE,
    PAGE_ERROR,
    REQUEST,
    RESPONSE,
)
from graphrecon.events.event_bus import EventBus


class BrowserEventHandlers:
    """
    Registers Playwright events and forwards them
    to the EventBus.
    """

    def __init__(
        self,
        page: Page,
        bus: EventBus,
    ) -> None:
        self.page = page
        self.bus = bus

    def register(self) -> None:
        """
        Register all browser events.
        """

        self.page.on("request", self._on_request)

        self.page.on("response", self._on_response)

        self.page.on("console", self._on_console)

        self.page.on("pageerror", self._on_page_error)

    def _on_request(self, request: Request) -> None:
        self.bus.emit(REQUEST, request)

    def _on_response(self, response: Response) -> None:
        self.bus.emit(RESPONSE, response)

    def _on_console(self, message: ConsoleMessage) -> None:
        self.bus.emit(CONSOLE, message)

    def _on_page_error(self, error: Exception) -> None:
        self.bus.emit(PAGE_ERROR, error)
