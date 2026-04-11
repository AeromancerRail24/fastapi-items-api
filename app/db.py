from collections import OrderedDict

from app.models.item import Item


_ITEMS = OrderedDict[int, Item]()
_LAST_ID = 0


def reset_items() -> None:
    """Clear all stored items for tests and manual resets."""

    global _LAST_ID
    _ITEMS.clear()
    _LAST_ID = 0


def create_item(item: Item) -> Item:
    global _LAST_ID
    _LAST_ID += 1
    stored = Item(id=_LAST_ID, name=item.name, description=item.description, price=item.price)
    _ITEMS[stored.id] = stored
    return stored


def list_items() -> list[Item]:
    return list(_ITEMS.values())


def get_item(item_id: int) -> Item | None:
    return _ITEMS.get(item_id)


def delete_item(item_id: int) -> bool:
    if item_id in _ITEMS:
        del _ITEMS[item_id]
        return True
    return False
