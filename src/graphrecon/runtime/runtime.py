from graphrecon.browser.browser_manager import BrowserManager
from graphrecon.collectors.dom.dom_collector import DOMCollector
from graphrecon.collectors.domain.domain_collector import DomainCollector
from graphrecon.collectors.page.page_collector import PageCollector
from graphrecon.collectors.request.request_collector import RequestCollector
from graphrecon.collectors.resource.resource_collector import ResourceCollector
from graphrecon.collectors.response.response_collector import ResponseCollector
from graphrecon.crawler.crawler import Crawler
from graphrecon.events.event_bus import EventBus
from graphrecon.graph.graph_builder import GraphBuilder
from graphrecon.storage.storage_manager import StorageManager
from graphrecon.utils.logger import logger


class Runtime:
    def __init__(self) -> None:
        self.event_bus = EventBus()

        self.browser = BrowserManager(self.event_bus)

        self.page_collector = PageCollector()
        self.request_collector = RequestCollector(self.event_bus)
        self.response_collector = ResponseCollector(self.event_bus)
        self.resource_collector = ResourceCollector(self.event_bus)

        self.domain_collector = DomainCollector()
        self.dom_collector = DOMCollector()

        # Crawl up to 25 pages (change later from config)
        self.crawler = Crawler(max_pages=25)

        self.storage = StorageManager()
        self.graph_builder = GraphBuilder()

        self.page_collector.register()
        self.request_collector.register()
        self.response_collector.register()
        self.resource_collector.register()

    def scan(self, url: str) -> None:
        self.resource_collector.set_target(url)

        self.browser.start()

        dom_resources = []

        try:
            discovered_pages = self.crawler.crawl(
                self.browser.page,
                url,
            )

            logger.info(
                "Discovered %d pages",
                len(discovered_pages),
            )

            # Collect page information
            for page_url in discovered_pages:

                self.browser.page.goto(
                    page_url,
                    wait_until="networkidle",
                )

                self.page_collector.collect_page(
                    self.browser.page,
                )

                dom_resources.extend(
                    self.dom_collector.collect(
                        self.browser.page,
                    )
                )

        finally:
            self.browser.stop()

        nodes, edges = self.graph_builder.build(
            self.page_collector.pages,
            self.resource_collector.resources,
            dom_resources,
        )

        domains = self.domain_collector.collect(
            self.resource_collector.resources,
        )

        self.storage.save_pages(self.page_collector.pages)
        self.storage.save_requests(self.request_collector.requests)
        self.storage.save_responses(self.response_collector.responses)
        self.storage.save_resources(self.resource_collector.resources)
        self.storage.save_domains(domains)
        self.storage.save_dom_resources(dom_resources)
        self.storage.save_graph(nodes, edges)
        self.storage.save_metadata(url)

        logger.info(
            "Pages crawled: %d",
            len(discovered_pages),
        )

        logger.info(
            "DOM resources: %d",
            len(dom_resources),
        )

        logger.info(
            "Graph: %d nodes, %d edges",
            len(nodes),
            len(edges),
        )

        logger.info(
            "Scan saved to %s",
            self.storage.scan_dir,
        )
