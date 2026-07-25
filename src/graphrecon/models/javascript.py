from graphrecon.models.base import GraphReconBaseModel


class JavaScriptModel(GraphReconBaseModel):
    """
    Represents a discovered JavaScript asset.
    """

    url: str

    filename: str

    domain: str

    third_party: bool

    minified: bool
