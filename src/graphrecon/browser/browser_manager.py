from playwright.sync_api import sync_playwright

from graphrecon.events.event_bus import EventBus
from graphrecon.utils.logger import logger


class BrowserManager:

    def __init__(self, bus: EventBus):

        self.bus = bus

    def open(self, url: str):

        with sync_playwright() as playwright:

            browser = playwright.chromium.launch(
                headless=True,
            )

            context = browser.new_context()

            page = context.new_page()

            page.goto(url)

            logger.info("Loaded %s", page.url)

            self.bus.emit(
                "page.loaded",
                page,
            )

            browser.close()
