# order_service/schemas.py

from pydantic import BaseModel
from typing import List

class OrderItemCreate(BaseModel):
    item_id: str
    quantity: int

class OrderCreate(BaseModel):
    user_id: str
    restaurant_id: str
    items: List[OrderItemCreate]

class OrderItemResponse(BaseModel):
    item_id: str
    quantity: int

class OrderResponse(BaseModel):
    id: str
    user_id: str
    restaurant_id: str
    items: List[OrderItemResponse]
    total_price: float

    class Config:
        orm_mode = True
