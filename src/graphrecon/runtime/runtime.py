from graphrecon.browser.browser_manager import BrowserManager
from graphrecon.collectors.domain.domain_collector import DomainCollector
from graphrecon.collectors.page.page_collector import PageCollector
from graphrecon.collectors.request.request_collector import RequestCollector
from graphrecon.collectors.resource.resource_collector import ResourceCollector
from graphrecon.collectors.response.response_collector import ResponseCollector
from graphrecon.events.event_bus import EventBus
from graphrecon.graph.graph_builder import GraphBuilder
from graphrecon.storage.storage_manager import StorageManager
from graphrecon.utils.logger import logger


class Runtime:
    """
    Coordinates the GraphRecon runtime.
    """

    def __init__(self) -> None:
        self.event_bus = EventBus()

        self.browser = BrowserManager(self.event_bus)

        self.page_collector = PageCollector()
        self.request_collector = RequestCollector(self.event_bus)
        self.response_collector = ResponseCollector(self.event_bus)
        self.resource_collector = ResourceCollector(self.event_bus)

        # Analysis collectors
        self.domain_collector = DomainCollector()

        self.storage = StorageManager()
        self.graph_builder = GraphBuilder()

        # Register event-based collectors
        self.page_collector.register()
        self.request_collector.register()
        self.response_collector.register()
        self.resource_collector.register()

    def scan(self, url: str) -> None:
        """
        Execute a scan.
        """

        self.resource_collector.set_target(url)

        self.browser.start()

        try:
            self.browser.open(url)

            self.page_collector.collect_page(
                self.browser.page,
            )

        finally:
            self.browser.stop()

        # Build dependency graph
        nodes, edges = self.graph_builder.build(
            self.page_collector.pages,
            self.resource_collector.resources,
        )

        # Build domain intelligence
        domains = self.domain_collector.collect(
            self.resource_collector.resources,
        )

        # Persist scan results
        self.storage.save_pages(
            self.page_collector.pages,
        )

        self.storage.save_requests(
            self.request_collector.requests,
        )

        self.storage.save_responses(
            self.response_collector.responses,
        )

        self.storage.save_resources(
            self.resource_collector.resources,
        )

        self.storage.save_domains(
            domains,
        )

        self.storage.save_graph(
            nodes,
            edges,
        )

        self.storage.save_metadata(
            url,
        )

        logger.info(
            "Graph: %d nodes, %d edges",
            len(nodes),
            len(edges),
        )

        logger.info(
            "Domains discovered: %d",
            len(domains),
        )

        logger.info(
            "Scan saved to %s",
            self.storage.scan_dir,
        )
