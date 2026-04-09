from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/health")
def healthcheck() -> dict[str, str]:
    return {
        "status": "ready",
        "service": "znxcpxmf",
    }
