from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    """Payload expected when creating an item."""

    name: str = Field(min_length=1, max_length=80)
    description: str | None = None
    price: float = Field(ge=0)
    available: bool = True


class ItemResponse(BaseModel):
    """Public response schema for item resources."""

    id: int
    name: str
    description: str | None = None
    price: float
    available: bool


class ItemUpdate(BaseModel):
    """Payload expected when mutating partial item fields."""

    name: str | None = Field(default=None, min_length=1, max_length=80)
    description: str | None = None
    price: float | None = Field(default=None, ge=0)
    available: bool | None = None
