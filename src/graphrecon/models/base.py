from pydantic import BaseModel, ConfigDict


class GraphReconBaseModel(BaseModel):
    """
    Base model inherited by every project model.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        frozen=False,
        str_strip_whitespace=True,
    )
