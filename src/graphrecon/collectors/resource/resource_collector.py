from urllib.parse import urlparse

from playwright.sync_api import Response

from graphrecon.browser.events import RESPONSE
from graphrecon.events.event_bus import EventBus
from graphrecon.models.resource import ResourceModel


class ResourceCollector:
    """
    Builds a normalized list of resources loaded by the page.
    """

    def __init__(self, event_bus: EventBus) -> None:
        self._event_bus = event_bus
        self.resources: list[ResourceModel] = []
        self._seen: set[str] = set()
        self._target_domain: str | None = None

    def register(self) -> None:
        self._event_bus.subscribe(RESPONSE, self._on_response)

    def set_target(self, url: str) -> None:
        self._target_domain = urlparse(url).netloc.lower()

    def _on_response(self, response: Response) -> None:

        url = response.url

        if url in self._seen:
            return

        self._seen.add(url)

        parsed = urlparse(url)

        domain = parsed.netloc.lower()

        content_type = response.headers.get("content-type")

        model = ResourceModel(
            url=url,
            domain=domain,
            resource_type=response.request.resource_type,
            content_type=content_type,
            third_party=(
                self._target_domain is not None
                and domain != self._target_domain
            ),
        )

        self.resources.append(model)
