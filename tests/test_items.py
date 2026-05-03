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
        "available": True,
    }


def test_get_item_by_id_returns_the_same_record() -> None:
    created = client.post(
        "/items",
        json={"name": "Blue pen", "description": "0.7mm", "price": 2.5},
    )

    response = client.get(f"/items/{created.json()['id']}")

    assert response.status_code == 200
    assert response.json() == created.json()


def test_delete_item_removes_item() -> None:
    created = client.post(
        "/items",
        json={"name": "Tape", "description": "Clear", "price": 3.3},
    )

    delete_response = client.delete(f"/items/{created.json()['id']}")
    assert delete_response.status_code == 204
    assert client.get(f"/items/{created.json()['id']}").status_code == 404


def test_missing_item_returns_404() -> None:
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item 999 does not exist"


def test_create_item_validation_error() -> None:
    response = client.post(
        "/items",
        json={"name": "", "description": "No name", "price": 5.0},
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "string_too_short"


def test_create_item_price_validation_error() -> None:
    response = client.post(
        "/items",
        json={"name": "Bad item", "description": "Too cheap", "price": -7.0},
    )

    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "greater_than_equal"
