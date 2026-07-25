from __future__ import annotations

from datetime import datetime
from pathlib import Path

import orjson

from graphrecon.models.page import PageModel


class StorageManager:
    """
    Handles scan output on disk.
    """

    def __init__(self) -> None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.scan_dir = Path(".scans") / timestamp

        self.scan_dir.mkdir(parents=True, exist_ok=True)

    def save_pages(self, pages: list[PageModel]) -> None:
        """
        Save collected pages.
        """

        output = self.scan_dir / "pages.json"

        data = [
            page.model_dump()
            for page in pages
        ]

        output.write_bytes(
            orjson.dumps(
                data,
                option=orjson.OPT_INDENT_2,
            )
        )

    def save_metadata(self, target: str) -> None:
        """
        Save scan metadata.
        """

        output = self.scan_dir / "metadata.json"

        metadata = {
            "target": target,
            "created_at": datetime.now().isoformat(),
            "version": "0.1.0",
        }

        output.write_bytes(
            orjson.dumps(
                metadata,
                option=orjson.OPT_INDENT_2,
            )
        )
