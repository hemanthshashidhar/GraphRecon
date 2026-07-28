from graphrecon.models.base import GraphReconBaseModel


class JavaScriptFindingModel(GraphReconBaseModel):
    finding_type: str
    value: str
    source: str
