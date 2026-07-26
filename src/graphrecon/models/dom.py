from graphrecon.models.base import GraphReconBaseModel


class DOMResourceModel(GraphReconBaseModel):
    """
    Represents one dependency discovered directly from the DOM.
    """

    tag: str

    attribute: str

    value: str
