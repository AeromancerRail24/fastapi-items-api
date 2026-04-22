from fastapi.testclient import TestClient

from app import db
from app.main import app


client = TestClient(app)


def setup_function() -> None:
    db.reset_items()


def test_list_items_starts_empty() -> None:
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item_persists_and_returns_payload() -> None:
    payload = {
        "name": "Starter notebook",
        "description": "Blue cover",
        "price": 19.5,
    }

    response = client.post("/items", json=payload)
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": "Starter notebook",
        "description": "Blue cover",
        "price": 19.5,
    }
