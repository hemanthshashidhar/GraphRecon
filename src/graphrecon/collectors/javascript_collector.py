from playwright.sync_api import Response

from graphrecon.events.event_bus import EventBus
from graphrecon.models.javascript_source import JavaScriptSourceModel


class JavaScriptCollector:
    """
    Collect JavaScript source directly from Playwright responses.
    """

    def __init__(self, event_bus: EventBus):

        self.sources: list[JavaScriptSourceModel] = []

        event_bus.subscribe(
            "response",
            self.handle_response,
        )

    def handle_response(
        self,
        response: Response,
    ) -> None:

        request = response.request

        if request.resource_type != "script":
            return

        try:
            source = response.text()
        except Exception:
            return

        self.sources.append(
            JavaScriptSourceModel(
                url=response.url,
                content=source,
            )
        )
