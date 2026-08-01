from graphrecon.models.base import GraphReconBaseModel


class JavaScriptFindingModel(GraphReconBaseModel):
    """
    Represents one interesting finding extracted
    from a JavaScript file.
    """

    finding_type: str

    value: str

    script_url: str
