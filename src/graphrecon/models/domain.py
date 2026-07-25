from graphrecon.models.base import GraphReconBaseModel


class DomainModel(GraphReconBaseModel):
    """
    Represents a unique domain contacted during a scan.
    """

    domain: str

    resource_count: int

    third_party: bool
