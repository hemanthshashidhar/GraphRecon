from graphrecon.models.edge import EdgeModel
from graphrecon.models.node import NodeModel
from graphrecon.models.page import PageModel
from graphrecon.models.resource import ResourceModel


IGNORED_RESOURCE_TYPES = {
    "document",
    "favicon",
}


class GraphBuilder:
    """
    Builds the dependency graph.
    """

    def build(
        self,
        pages: list[PageModel],
        resources: list[ResourceModel],
    ) -> tuple[list[NodeModel], list[EdgeModel]]:

        nodes: list[NodeModel] = []

        edges: list[EdgeModel] = []

        node_ids: set[str] = set()

        if not pages:
            return nodes, edges

        page = pages[0]

        page_id = page.url

        nodes.append(
            NodeModel(
                id=page_id,
                type="page",
                label=page.title,
            )
        )

        node_ids.add(page_id)

        for resource in resources:

            if resource.resource_type in IGNORED_RESOURCE_TYPES:
                continue

            if resource.url not in node_ids:

                nodes.append(
                    NodeModel(
                        id=resource.url,
                        type=resource.resource_type,
                        label=resource.url,
                    )
                )

                node_ids.add(resource.url)

            edges.append(
                EdgeModel(
                    source=page_id,
                    target=resource.url,
                    relationship="loads",
                )
            )

        return nodes, edges
