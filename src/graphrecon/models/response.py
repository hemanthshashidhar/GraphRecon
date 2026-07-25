from graphrecon.models.base import GraphReconBaseModel


class ResponseModel(GraphReconBaseModel):
    """
    Represents a browser network response.
    """

    url: str

    status: int

    status_text: str

    resource_type: str

    headers: dict[str, str]

    ok: bool
