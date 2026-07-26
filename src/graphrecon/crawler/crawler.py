from playwright.sync_api import Page

from graphrecon.crawler.link_extractor import LinkExtractor
from graphrecon.crawler.url_queue import URLQueue


class Crawler:
    """
    Simple breadth-first crawler.
    """

    def __init__(
        self,
        max_pages: int = 25,
    ) -> None:

        self.max_pages = max_pages

        self.queue = URLQueue()

        self.extractor = LinkExtractor()

    def crawl(
        self,
        page: Page,
        start_url: str,
    ) -> list[str]:

        discovered: list[str] = []

        self.queue.add(start_url)

        while not self.queue.empty():

            if len(discovered) >= self.max_pages:
                break

            url = self.queue.pop()

            page.goto(
                url,
                wait_until="networkidle",
            )

            discovered.append(url)

            for link in self.extractor.extract(
                page,
                url,
            ):
                self.queue.add(link)

        return discovered
