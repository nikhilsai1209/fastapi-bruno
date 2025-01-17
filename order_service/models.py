# order_service/models.py

from beanie import Document
from pydantic import BaseModel, Field
from typing import List

class OrderItem(BaseModel):
    item_id: str = Field(..., description="The ID of the item")
    quantity: int = Field(..., gt=0, description="Quantity of the item ordered")

class Order(Document):
    user_id: str = Field(..., description="The ID of the user placing the order")
    restaurant_id: str = Field(..., description="The ID of the restaurant")
    items: List[OrderItem] = Field(..., description="List of items in the order")
    total_price: float = Field(0.0, description="Total price of the order")

    class Settings:
        name = "orders"  # MongoDB collection name
