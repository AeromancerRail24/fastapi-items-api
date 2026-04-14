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
