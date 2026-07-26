from __future__ import annotations

from datetime import datetime
from pathlib import Path

import orjson

from graphrecon.models.dom import DOMResourceModel
from graphrecon.models.domain import DomainModel
from graphrecon.models.edge import EdgeModel
from graphrecon.models.node import NodeModel
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
        (self.scan_dir / filename).write_bytes(
            orjson.dumps(
                data,
                option=orjson.OPT_INDENT_2,
            )
        )

    def save_pages(self, pages: list[PageModel]) -> None:
        self._write_json("pages.json", [p.model_dump() for p in pages])

    def save_requests(self, requests: list[RequestModel]) -> None:
        self._write_json("requests.json", [r.model_dump() for r in requests])

    def save_responses(self, responses: list[ResponseModel]) -> None:
        self._write_json("responses.json", [r.model_dump() for r in responses])

    def save_resources(self, resources: list[ResourceModel]) -> None:
        self._write_json("resources.json", [r.model_dump() for r in resources])

    def save_domains(self, domains: list[DomainModel]) -> None:
        self._write_json("domains.json", [d.model_dump() for d in domains])

    def save_dom_resources(
        self,
        resources: list[DOMResourceModel],
    ) -> None:
        self._write_json(
            "dom_resources.json",
            [r.model_dump() for r in resources],
        )

    def save_graph(
        self,
        nodes: list[NodeModel],
        edges: list[EdgeModel],
    ) -> None:
        self._write_json(
            "graph.json",
            {
                "nodes": [n.model_dump() for n in nodes],
                "edges": [e.model_dump() for e in edges],
            },
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
