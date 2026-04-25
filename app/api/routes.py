from fastapi import APIRouter, HTTPException, status

from app.schemas.item import ItemCreate, ItemResponse
from app.services.item_service import ItemNotFoundError, ItemService

api_router = APIRouter()


def _item_service() -> ItemService:
    return ItemService()


def _not_found(error: Exception) -> None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@api_router.get("/health", tags=["system"])
def healthcheck() -> dict[str, str]:
    return {
        "status": "ready",
        "service": "znxcpxmf",
    }


@api_router.get(
    "/items",
    response_model=list[ItemResponse],
    tags=["items"],
)
def list_items() -> list[ItemResponse]:
    service = _item_service()
    return service.list_items()


@api_router.post(
    "/items",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["items"],
)
def create_item(payload: ItemCreate) -> ItemResponse:
    service = _item_service()
    return service.create_item(payload)


@api_router.get(
    "/items/{item_id}",
    response_model=ItemResponse,
    tags=["items"],
)
def get_item(item_id: int) -> ItemResponse:
    service = _item_service()
    try:
        return service.get_item(item_id)
    except ItemNotFoundError as error:
        _not_found(error)


@api_router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["items"])
def delete_item(item_id: int) -> None:
    service = _item_service()
    try:
        service.delete_item(item_id)
    except ItemNotFoundError as error:
        _not_found(error)
