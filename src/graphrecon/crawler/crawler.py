from collections.abc import Generator

from playwright.sync_api import Page

from graphrecon.crawler.link_extractor import LinkExtractor
from graphrecon.crawler.url_queue import URLQueue


class Crawler:
    """
    Breadth-first crawler.

    Yields each loaded page exactly once.
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
    ) -> Generator[Page, None, None]:

        self.queue.add(start_url, depth=0)

        pages_crawled = 0

        while not self.queue.empty():

            if pages_crawled >= self.max_pages:
                break

            item = self.queue.pop()

            page.goto(
                item.url,
                wait_until="networkidle",
            )

            pages_crawled += 1

            yield page

            for link in self.extractor.extract(
                page,
                item.url,
            ):
                self.queue.add(
                    link,
                    depth=item.depth + 1,
                )
