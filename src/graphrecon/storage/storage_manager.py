from __future__ import annotations

from datetime import datetime
from pathlib import Path

import orjson

from graphrecon.models.page import PageModel
from graphrecon.models.request import RequestModel
from graphrecon.models.resource import ResourceModel
from graphrecon.models.response import ResponseModel


class StorageManager:
    def __init__(self) -> None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.scan_dir = Path(".scans") / timestamp

        self.scan_dir.mkdir(parents=True, exist_ok=True)

    def _write_json(self, filename: str, data: object) -> None:
        output = self.scan_dir / filename

        output.write_bytes(
            orjson.dumps(
                data,
                option=orjson.OPT_INDENT_2,
            )
        )

    def save_pages(self, pages: list[PageModel]) -> None:
        self._write_json(
            "pages.json",
            [page.model_dump() for page in pages],
        )

    def save_requests(self, requests: list[RequestModel]) -> None:
        self._write_json(
            "requests.json",
            [request.model_dump() for request in requests],
        )

    def save_responses(self, responses: list[ResponseModel]) -> None:
        self._write_json(
            "responses.json",
            [response.model_dump() for response in responses],
        )

    def save_resources(self, resources: list[ResourceModel]) -> None:
        self._write_json(
            "resources.json",
            [resource.model_dump() for resource in resources],
        )

    def save_metadata(self, target: str) -> None:
        self._write_json(
            "metadata.json",
            {
                "target": target,
                "created_at": datetime.now().isoformat(),
                "version": "0.1.0",
            },
        )
