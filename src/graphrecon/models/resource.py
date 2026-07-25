from graphrecon.models.base import GraphReconBaseModel


class ResourceModel(GraphReconBaseModel):
    """
    Represents a loaded browser resource.
    """

    url: str

    domain: str

    resource_type: str

    content_type: str | None = None

    third_party: bool
