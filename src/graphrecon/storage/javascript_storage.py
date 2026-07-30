import json
from pathlib import Path


class JavaScriptStorage:

    def save(
        self,
        findings: list[dict],
        scan_dir: Path,
    ) -> None:

        output = scan_dir / "javascript_findings.json"

        output.write_text(
            json.dumps(
                findings,
                indent=2,
            ),
            encoding="utf-8",
        )
