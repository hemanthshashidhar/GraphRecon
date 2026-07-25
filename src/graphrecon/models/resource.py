from graphrecon.models.base import GraphReconBaseModel


class ResourceModel(GraphReconBaseModel):
    """
    Represents one loaded resource.
    """

    url: str

    domain: str

    path: str

    filename: str

    extension: str

    scheme: str

    resource_type: str

    content_type: str | None = None

    third_party: bool
