from app import db
from app.models.item import Item
from app.schemas.item import ItemCreate


class ItemNotFoundError(KeyError):
    pass


class ItemService:
    def list_items(self) -> list[Item]:
        return db.list_items()

    def get_item(self, item_id: int) -> Item:
        item = db.get_item(item_id)
        if item is None:
            raise ItemNotFoundError(f"Item {item_id} does not exist")
        return item

    def create_item(self, payload: ItemCreate) -> Item:
        return db.create_item(
            Item(
                id=0,
                name=payload.name,
                description=payload.description,
                price=payload.price,
            )
        )

    def delete_item(self, item_id: int) -> None:
        deleted = db.delete_item(item_id)
        if not deleted:
            raise ItemNotFoundError(f"Item {item_id} does not exist")
