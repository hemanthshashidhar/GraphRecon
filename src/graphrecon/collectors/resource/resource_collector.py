from pathlib import PurePosixPath
from urllib.parse import urlparse

from playwright.sync_api import Response

from graphrecon.browser.events import RESPONSE
from graphrecon.events.event_bus import EventBus
from graphrecon.models.resource import ResourceModel


RESOURCE_CATEGORY = {
    "script": "javascript",
    "stylesheet": "css",
    "image": "image",
    "font": "font",
    "xhr": "api",
    "fetch": "api",
    "websocket": "websocket",
    "media": "media",
    "manifest": "manifest",
    "document": "document",
}


class ResourceCollector:
    """
    Collects browser resources.
    """

    def __init__(self, event_bus: EventBus) -> None:
        self._event_bus = event_bus
        self.resources: list[ResourceModel] = []
        self._seen: set[str] = set()
        self._target_domain: str | None = None

    def register(self) -> None:
        self._event_bus.subscribe(
            RESPONSE,
            self._on_response,
        )

    def set_target(self, url: str) -> None:
        self._target_domain = urlparse(url).netloc.lower()

    def _on_response(self, response: Response) -> None:

        if response.url in self._seen:
            return

        self._seen.add(response.url)

        parsed = urlparse(response.url)

        filename = PurePosixPath(parsed.path).name

        extension = PurePosixPath(parsed.path).suffix.lower()

        self.resources.append(
            ResourceModel(
                url=response.url,
                domain=parsed.netloc.lower(),
                path=parsed.path,
                filename=filename,
                extension=extension,
                scheme=parsed.scheme,
                resource_type=response.request.resource_type,
                category=RESOURCE_CATEGORY.get(
                    response.request.resource_type,
                    "other",
                ),
                content_type=response.headers.get("content-type"),
                third_party=(
                    self._target_domain is not None
                    and parsed.netloc.lower() != self._target_domain
                ),
            )
        )
