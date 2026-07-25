from __future__ import annotations

from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)

from graphrecon.browser.event_handlers import BrowserEventHandlers
from graphrecon.config.settings import settings
from graphrecon.events.event_bus import EventBus
from graphrecon.utils.logger import logger


class BrowserManager:
    """
    Browser lifecycle manager.
    """

    def __init__(self, event_bus: EventBus) -> None:
        self.event_bus = event_bus

        self._playwright: Playwright | None = None
        self._browser: Browser | None = None
        self._context: BrowserContext | None = None
        self._page: Page | None = None

    def start(self) -> None:
        logger.info("Starting Playwright...")

        self._playwright = sync_playwright().start()

        self._browser = self._playwright.chromium.launch(
            headless=settings.browser_headless,
        )

        self._context = self._browser.new_context()

        self._page = self._context.new_page()

        BrowserEventHandlers(
            page=self._page,
            bus=self.event_bus,
        ).register()

        logger.info("Browser started.")

    def open(self, url: str) -> None:
        if self._page is None:
            raise RuntimeError("Browser has not been started.")

        logger.info("Opening %s", url)

        self._page.goto(
            url,
            timeout=settings.timeout,
            wait_until="networkidle",
        )

        logger.info("Loaded %s", self._page.url)

    @property
    def page(self) -> Page:
        if self._page is None:
            raise RuntimeError("Page not initialized.")
        return self._page

    def stop(self) -> None:
        logger.info("Closing browser...")

        if self._context:
            self._context.close()

        if self._browser:
            self._browser.close()

        if self._playwright:
            self._playwright.stop()

        logger.info("Browser closed.")
