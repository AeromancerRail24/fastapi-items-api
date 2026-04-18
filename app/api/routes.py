from fastapi import APIRouter, HTTPException, status

from app.schemas.item import ItemCreate, ItemResponse

api_router = APIRouter()


def _not_found(error: Exception) -> None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))


@api_router.get("/health")
def healthcheck() -> dict[str, str]:
    return {
        "status": "ready",
        "service": "znxcpxmf",
    }


@api_router.get("/items", response_model=list[ItemResponse], tags=["items"])
def list_items() -> list[ItemResponse]:
    from app.services.item_service import ItemService

    service = ItemService()
    return service.list_items()


@api_router.post("/items", response_model=ItemResponse, status_code=201, tags=["items"])
def create_item(payload: ItemCreate) -> ItemResponse:
    from app.services.item_service import ItemService

    service = ItemService()
    return service.create_item(payload)


@api_router.get("/items/{item_id}", response_model=ItemResponse, tags=["items"])
def get_item(item_id: int) -> ItemResponse:
    from app.services.item_service import ItemNotFoundError, ItemService

    service = ItemService()
    try:
        return service.get_item(item_id)
    except ItemNotFoundError as error:
        _not_found(error)


@api_router.delete("/items/{item_id}", status_code=204, tags=["items"])
def delete_item(item_id: int) -> None:
    from app.services.item_service import ItemNotFoundError, ItemService

    service = ItemService()
    try:
        service.delete_item(item_id)
    except ItemNotFoundError as error:
        _not_found(error)
