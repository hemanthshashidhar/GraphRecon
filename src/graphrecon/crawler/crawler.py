from playwright.sync_api import Page

from graphrecon.crawler.link_extractor import LinkExtractor
from graphrecon.crawler.url_queue import URLQueue


class Crawler:
    """
    Breadth-first crawler.
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

        self.queue.add(start_url, depth=0)

        while not self.queue.empty():

            if len(discovered) >= self.max_pages:
                break

            item = self.queue.pop()

            page.goto(
                item.url,
                wait_until="networkidle",
            )

            discovered.append(item.url)

            links = self.extractor.extract(
                page,
                item.url,
            )

            for link in links:
                self.queue.add(
                    link,
                    depth=item.depth + 1,
                )

        return discovered
