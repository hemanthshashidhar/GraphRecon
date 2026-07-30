import re

from playwright.sync_api import Response

from graphrecon.cache.response_cache import ResponseCache


class JavaScriptAnalyzer:
    """
    Analyze JavaScript responses captured by Playwright.
    """

    PATTERNS = {
        "fetch": r'fetch\s*\(\s*[\'"]([^\'"]+)',
        "axios": r'axios\.(?:get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)',
        "xhr": r'open\s*\(\s*[\'"][A-Z]+[\'"]\s*,\s*[\'"]([^\'"]+)',
        "websocket": r'new\s+WebSocket\s*\(\s*[\'"]([^\'"]+)',
        "graphql": r"/graphql",
        "dynamic_import": r'import\s*\(\s*[\'"]([^\'"]+)',
    }

    def __init__(
        self,
        cache: ResponseCache,
    ) -> None:

        self.cache = cache

    def analyze(self) -> list[dict]:

        findings = []

        for response in self.cache.all():

            request = response.request

            if request.resource_type != "script":
                continue

            try:
                source = response.text()
            except Exception:
                continue

            for finding_type, pattern in self.PATTERNS.items():

                for match in re.findall(
                    pattern,
                    source,
                ):

                    findings.append(
                        {
                            "type": finding_type,
                            "value": match,
                            "script": response.url,
                        }
                    )

        return findings
