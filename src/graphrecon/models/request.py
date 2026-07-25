from graphrecon.models.base import GraphReconBaseModel


class RequestModel(GraphReconBaseModel):
    """
    Represents a browser network request.
    """

    method: str

    url: str

    resource_type: str

    is_navigation: bool

    headers: dict[str, str]
