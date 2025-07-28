from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: int
    name: str
    price: float
    stock: int

class ItemCreate(BaseModel):
    name: str
    price: float
    stock: int
    
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
