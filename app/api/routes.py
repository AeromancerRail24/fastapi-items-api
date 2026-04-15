from fastapi import APIRouter

from app.schemas.item import ItemCreate, ItemResponse

api_router = APIRouter()


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
    return service.get_item(item_id)
