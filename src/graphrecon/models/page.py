from graphrecon.models.base import GraphReconBaseModel


class PageModel(GraphReconBaseModel):
    """
    Represents a visited page.
    """

    url: str

    final_url: str

    title: str

    status: int | None = None
