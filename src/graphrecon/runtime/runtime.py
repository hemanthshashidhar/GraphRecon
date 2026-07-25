from graphrecon.browser.browser_manager import BrowserManager
from graphrecon.collectors.page.page_collector import PageCollector
from graphrecon.collectors.request.request_collector import RequestCollector
from graphrecon.collectors.response.response_collector import ResponseCollector
from graphrecon.events.event_bus import EventBus
from graphrecon.storage.storage_manager import StorageManager
from graphrecon.utils.logger import logger


class Runtime:
    """
    Coordinates GraphRecon runtime.
    """

    def __init__(self) -> None:
        self.event_bus = EventBus()

        self.browser = BrowserManager(self.event_bus)

        self.page_collector = PageCollector()

        self.request_collector = RequestCollector(self.event_bus)

        self.response_collector = ResponseCollector(self.event_bus)

        self.storage = StorageManager()

        self.page_collector.register()
        self.request_collector.register()
        self.response_collector.register()

    def scan(self, url: str) -> None:
        self.browser.start()

        try:
            self.browser.open(url)

            self.page_collector.collect_page(
                self.browser.page,
            )

        finally:
            self.browser.stop()

        self.storage.save_pages(
            self.page_collector.pages,
        )

        self.storage.save_requests(
            self.request_collector.requests,
        )

        self.storage.save_responses(
            self.response_collector.responses,
        )

        self.storage.save_metadata(
            url,
        )

        logger.info(
            "Scan saved to %s",
            self.storage.scan_dir,
        )
