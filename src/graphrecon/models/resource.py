from graphrecon.models.base import GraphReconBaseModel


class ResourceModel(GraphReconBaseModel):
    """
    Represents a loaded browser resource.
    """

    url: str

    domain: str

    path: str

    filename: str

    extension: str

    scheme: str

    resource_type: str

    category: str

    content_type: str | None = None

    third_party: bool
