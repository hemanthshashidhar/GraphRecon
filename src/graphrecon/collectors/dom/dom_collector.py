from playwright.sync_api import Page

from graphrecon.models.dom import DOMResourceModel


class DOMCollector:
    """
    Collects dependency declarations from the rendered DOM.
    """

    def collect(
        self,
        page: Page,
    ) -> list[DOMResourceModel]:

        script_urls = page.eval_on_selector_all(
            "script[src]",
            "els => els.map(e => e.src)",
        )

        stylesheet_urls = page.eval_on_selector_all(
            "link[rel='stylesheet']",
            "els => els.map(e => e.href)",
        )

        image_urls = page.eval_on_selector_all(
            "img[src]",
            "els => els.map(e => e.src)",
        )

        iframe_urls = page.eval_on_selector_all(
            "iframe[src]",
            "els => els.map(e => e.src)",
        )

        resources: list[DOMResourceModel] = []

        for url in script_urls:
            resources.append(
                DOMResourceModel(
                    tag="script",
                    attribute="src",
                    value=url,
                )
            )

        for url in stylesheet_urls:
            resources.append(
                DOMResourceModel(
                    tag="link",
                    attribute="href",
                    value=url,
                )
            )

        for url in image_urls:
            resources.append(
                DOMResourceModel(
                    tag="img",
                    attribute="src",
                    value=url,
                )
            )

        for url in iframe_urls:
            resources.append(
                DOMResourceModel(
                    tag="iframe",
                    attribute="src",
                    value=url,
                )
            )

        return resources
