from graphrecon.models.base import GraphReconBaseModel


class EdgeModel(GraphReconBaseModel):
    """
    A graph edge.
    """

    source: str

    target: str

    relationship: str
