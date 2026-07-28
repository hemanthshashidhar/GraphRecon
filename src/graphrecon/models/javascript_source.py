from graphrecon.models.base import GraphReconBaseModel


class JavaScriptSourceModel(GraphReconBaseModel):
    url: str
    content: str
