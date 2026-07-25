from graphrecon.models.base import GraphReconBaseModel


class NodeModel(GraphReconBaseModel):
    """
    A graph node.
    """

    id: str

    type: str

    label: str
