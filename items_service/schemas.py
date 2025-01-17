# items_service/schemas.py

from pydantic import BaseModel
from typing import Optional
from beanie import PydanticObjectId

class ItemCreate(BaseModel):
    name: str
    description: str
    price: int
    restaurant_id: PydanticObjectId  # Use PydanticObjectId

class ItemResponse(ItemCreate):
    id: PydanticObjectId  # Use PydanticObjectId

    class Config:
        orm_mode = True
