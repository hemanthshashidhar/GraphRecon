from graphrecon.browser.browser_manager import BrowserManager
from graphrecon.collectors.page.page_collector import PageCollector
from graphrecon.events.event_bus import EventBus


class Runtime:
    """
    Coordinates GraphRecon runtime.
    """

    def __init__(self) -> None:
        self.event_bus = EventBus()

        self.browser = BrowserManager(self.event_bus)

        self.page_collector = PageCollector(self.event_bus)

        self.page_collector.register()

    def scan(self, url: str) -> None:
        self.browser.start()

        try:
            self.browser.open(url)

            self.page_collector.collect_page(
                self.browser.page,
            )

        finally:
            self.browser.stop()
