import re

from graphrecon.models.javascript import JavaScriptFindingModel


class JavaScriptAnalyzer:
    """
    Static JavaScript analyzer.
    """

    PATTERNS = {
        "fetch": r'fetch\s*\(\s*["\']([^"\']+)["\']',
        "axios": r'axios\.(?:get|post|put|delete|patch)\s*\(\s*["\']([^"\']+)["\']',
        "xhr": r'open\s*\(\s*["\'][A-Z]+["\']\s*,\s*["\']([^"\']+)["\']',
        "websocket": r'new\s+WebSocket\s*\(\s*["\']([^"\']+)["\']',
        "eventsource": r'new\s+EventSource\s*\(\s*["\']([^"\']+)["\']',
        "import": r'import\s+.*?from\s+["\']([^"\']+)["\']',
        "dynamic_import": r'import\s*\(\s*["\']([^"\']+)["\']',
        "url": r'https?://[^\s"\']+',
    }

    def analyze(
        self,
        source: str,
        script_url: str,
    ) -> list[JavaScriptFindingModel]:

        findings = []

        for finding_type, pattern in self.PATTERNS.items():

            for match in re.findall(pattern, source):

                findings.append(
                    JavaScriptFindingModel(
                        finding_type=finding_type,
                        value=match,
                        source=script_url,
                    )
                )

        return findings
