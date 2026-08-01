import re

from playwright.sync_api import Response

from graphrecon.cache.response_cache import ResponseCache
from graphrecon.models.javascript_finding import JavaScriptFindingModel


class JavaScriptAnalyzer:
    """
    Analyze JavaScript responses captured by Playwright.
    """

    PATTERNS = {
        "fetch": r'fetch\s*\(\s*[\'"]([^\'"]+)',
        "axios": r'axios\.(?:get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)',
        "xhr": r'open\s*\(\s*[\'"][A-Z]+[\'"]\s*,\s*[\'"]([^\'"]+)',
        "websocket": r'new\s+WebSocket\s*\(\s*[\'"]([^\'"]+)',
        "eventsource": r'new\s+EventSource\s*\(\s*[\'"]([^\'"]+)',
        "dynamic_import": r'import\s*\(\s*[\'"]([^\'"]+)',
        "graphql": r'["\']([^"\']*/graphql[^"\']*)["\']',
    }

    def __init__(
        self,
        cache: ResponseCache,
    ) -> None:
        self.cache = cache

    def analyze(
        self,
    ) -> list[JavaScriptFindingModel]:

        findings: list[JavaScriptFindingModel] = []

        for response in self.cache.all():

            request = response.request

            if request.resource_type != "script":
                continue

            try:
                source = response.text()
            except Exception:
                continue

            for finding_type, pattern in self.PATTERNS.items():

                for match in re.findall(pattern, source):

                    findings.append(
                        JavaScriptFindingModel(
                            finding_type=finding_type,
                            value=match,
                            script_url=response.url,
                        )
                    )

        return findings
