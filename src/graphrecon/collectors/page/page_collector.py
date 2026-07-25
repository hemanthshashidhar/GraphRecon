from playwright.sync_api import Page

from graphrecon.models.page import PageModel
from graphrecon.utils.logger import logger


class PageCollector:
    """
    Collects page metadata only.
    """

    def __init__(self) -> None:
        self.pages: list[PageModel] = []

    def register(self) -> None:
        """
        Reserved for future page events.
        """

    def collect_page(self, page: Page) -> None:

        model = PageModel(
            url=page.url,
            final_url=page.url,
            title=page.title(),
        )

        self.pages.append(model)

        logger.info(
            "[PAGE] %s",
            model.title,
        )
