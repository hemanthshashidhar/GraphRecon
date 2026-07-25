from graphrecon.models.javascript import JavaScriptModel
from graphrecon.models.resource import ResourceModel


class JavaScriptAnalyzer:
    """
    Extract JavaScript assets from collected resources.
    """

    def analyze(
        self,
        resources: list[ResourceModel],
    ) -> list[JavaScriptModel]:

        results: list[JavaScriptModel] = []

        for resource in resources:

            if resource.resource_type != "script":
                continue

            results.append(
                JavaScriptModel(
                    url=resource.url,
                    filename=resource.filename,
                    domain=resource.domain,
                    third_party=resource.third_party,
                    minified=".min." in resource.filename.lower(),
                )
            )

        return results
