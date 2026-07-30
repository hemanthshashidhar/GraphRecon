from playwright.sync_api import Response


class ResponseCache:
    """
    Stores browser responses for later analysis.
    """

    def __init__(self) -> None:
        self._responses: dict[str, Response] = {}

    def add(self, response: Response) -> None:
        self._responses[response.url] = response

    def get(self, url: str) -> Response | None:
        return self._responses.get(url)

    def all(self) -> list[Response]:
        return list(self._responses.values())

    def clear(self) -> None:
        self._responses.clear()
