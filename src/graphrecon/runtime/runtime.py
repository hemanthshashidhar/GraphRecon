from graphrecon.browser.browser_manager import BrowserManager
from graphrecon.events.event_bus import EventBus


class Runtime:
    """
    Coordinates the GraphRecon runtime.
    """

    def __init__(self) -> None:
        self.event_bus = EventBus()
        self.browser = BrowserManager(self.event_bus)

    def scan(self, url: str) -> None:
        """
        Execute a scan.
        """
        self.browser.open(url)
