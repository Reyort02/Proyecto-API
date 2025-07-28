from fastapi import APIRouter, Request, HTTPException
from src.models.item import ItemCreate, Item, ItemUpdate
from src.services.item_service import create_item, get_items, delete_item, update_item

router = APIRouter()

@router.post("/items/", response_model=Item)
def add_item(item: ItemCreate, request: Request):
    current_user = request.state.user
    return create_item(item, current_user)

@router.get("/items/", response_model=list[Item])
def read_items(request: Request):
    current_user = request.state.user
    items = get_items()
    user_items = [i for i in items if i['owner']['sub'] == current_user['sub']]
    return user_items

@router.delete("/items/{item_id}", response_model=Item)
def remove_item(item_id: int, request: Request):
    current_user = request.state.user
    try:
        return delete_item(item_id, current_user['sub'])
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/items/{item_id}", response_model=Item)
def modify_item(item_id: int, item_update: ItemUpdate, request: Request):
    current_user = request.state.user
    try:
        return update_item(item_id, item_update, current_user['sub'])
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))