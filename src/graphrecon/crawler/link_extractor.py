from urllib.parse import urldefrag, urljoin, urlparse

from playwright.sync_api import Page


class LinkExtractor:
    """
    Extracts internal links from the current page.
    """

    def extract(
        self,
        page: Page,
        base_url: str,
    ) -> list[str]:

        hrefs = page.eval_on_selector_all(
            "a[href]",
            "els => els.map(e => e.getAttribute('href'))",
        )

        base_domain = urlparse(base_url).netloc

        links: set[str] = set()

        for href in hrefs:

            if not href:
                continue

            absolute = urljoin(base_url, href)

            absolute, _ = urldefrag(absolute)

            parsed = urlparse(absolute)

            if parsed.scheme not in ("http", "https"):
                continue

            if parsed.netloc != base_domain:
                continue

            links.add(absolute)

        return sorted(links)
