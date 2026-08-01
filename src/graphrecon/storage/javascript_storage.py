import json
from pathlib import Path

from graphrecon.models.javascript_finding import JavaScriptFindingModel


class JavaScriptStorage:

    def save(
        self,
        findings: list[JavaScriptFindingModel],
        scan_dir: Path,
    ) -> None:

        output = scan_dir / "javascript_findings.json"

        output.write_text(
            json.dumps(
                [
                    finding.model_dump()
                    for finding in findings
                ],
                indent=2,
            ),
            encoding="utf-8",
        )
