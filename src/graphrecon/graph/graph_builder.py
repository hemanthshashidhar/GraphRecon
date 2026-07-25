from graphrecon.models.edge import EdgeModel
from graphrecon.models.node import NodeModel
from graphrecon.models.page import PageModel
from graphrecon.models.resource import ResourceModel


class GraphBuilder:
    """
    Builds a dependency graph from collected models.
    """

    def build(
        self,
        pages: list[PageModel],
        resources: list[ResourceModel],
    ) -> tuple[list[NodeModel], list[EdgeModel]]:

        nodes: list[NodeModel] = []

        edges: list[EdgeModel] = []

        seen_nodes: set[str] = set()

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

        seen_nodes.add(page_id)

        for resource in resources:

            resource_id = resource.url

            if resource_id not in seen_nodes:

                nodes.append(
                    NodeModel(
                        id=resource_id,
                        type=resource.resource_type,
                        label=resource.url,
                    )
                )

                seen_nodes.add(resource_id)

            edges.append(
                EdgeModel(
                    source=page_id,
                    target=resource_id,
                    relationship="loads",
                )
            )

        return nodes, edges
