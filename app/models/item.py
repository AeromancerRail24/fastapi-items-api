from pydantic import BaseModel, Field


class Item(BaseModel):
    """Persisted item payload."""

    id: int
    name: str = Field(min_length=1)
    description: str | None = None
    price: float = Field(ge=0)
    available: bool = True
