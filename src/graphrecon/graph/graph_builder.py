from graphrecon.models.dom import DOMResourceModel
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
    Builds the dependency graph using DOM relationships whenever possible.
    """

    def build(
        self,
        pages: list[PageModel],
        resources: list[ResourceModel],
        dom_resources: list[DOMResourceModel],
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

        resource_lookup = {
            resource.url: resource
            for resource in resources
        }

        for dom in dom_resources:

            resource = resource_lookup.get(dom.value)

            if resource is None:
                continue

            if resource.resource_type in IGNORED_RESOURCE_TYPES:
                continue

            if resource.url not in node_ids:

                nodes.append(
                    NodeModel(
                        id=resource.url,
                        type=resource.category,
                        label=resource.filename
                        or resource.url,
                    )
                )

                node_ids.add(resource.url)

            edges.append(
                EdgeModel(
                    source=page_id,
                    target=resource.url,
                    relationship=dom.tag,
                )
            )

        return nodes, edges
