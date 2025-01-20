# items_service/routes.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from items_service.models import Item, PydanticObjectId
from items_service.schemas import ItemCreate, ItemResponse
from restaurant_service.models import Restaurant  # Adjust the import path as needed

router = APIRouter()

@router.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    restaurant = await Restaurant.get(item.restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    
    new_item = Item(**item.dict())
    await new_item.insert()
    return ItemResponse(id=new_item.id, **item.dict())

@router.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: PydanticObjectId):
    item = await Item.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return ItemResponse(id=item.id, name=item.name, description=item.description, price=item.price, restaurant_id=item.restaurant_id)

@router.get("/items/restaurant/{restaurant_id}", response_model=List[ItemResponse], status_code=status.HTTP_200_OK)
async def get_items_by_restaurant(restaurant_id: PydanticObjectId):
    items = await Item.find(Item.restaurant_id == restaurant_id).to_list()
    if not items:
        raise HTTPException(status_code=404, detail="No items found for this restaurant")
    
    return [ItemResponse(id=item.id, name=item.name, description=item.description, price=item.price, restaurant_id=item.restaurant_id) for item in items]

@router.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: PydanticObjectId):
    item = await Item.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    await item.delete()
    return {"message": "Item deleted successfully"}
