import json
from src.models.item import ItemCreate, ItemUpdate

ITEM_DB_FILE = "src/data/items.json"

def get_items():
    try:
        with open(ITEM_DB_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_items(items):
    with open(ITEM_DB_FILE, "w") as f:
        json.dump(items, f, indent=4)
        
def get_next_id(items: list) -> int:
    return max((item.get('id', 0) for item in items), default=0) + 1

def create_item(item: ItemCreate, user_email: str):
    items = get_items()
    item_data = item.model_dump()
    item_data['owner'] = user_email
    item_data['id'] = get_next_id(items)
    items.append(item_data)
    save_items(items)
    return item_data

def delete_item(item_id: int, user_email: str):
    items = get_items()
    for i, item in enumerate(items):
        if item["id"] == item_id and item["owner"]['sub'] == user_email:
            deleted_item = items.pop(i)
            save_items(items)
            return deleted_item
    raise ValueError("Objeto no encontrado o no pertenece al usuario.")

def update_item(item_id: int, item_update: ItemUpdate, user_email: str):
    items = get_items()
    for item in items:
        if item["id"] == item_id and item["owner"]['sub'] == user_email:
            item.update(item_update.model_dump())
            save_items(items)
            return item
    raise ValueError("Objeto no encontrado o no pertenece al usuario.")