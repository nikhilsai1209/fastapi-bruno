from fastapi import APIRouter, HTTPException, status
from catalog_service.models import Items
from catalog_service.schemas import ItemCreate, ItemResponse
from bson import ObjectId

router = APIRouter()

@router.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    new_item = Items(**item.dict())
    await new_item.insert()  # Save to the database
    return ItemResponse(id=str(new_item.id), **item.dict())

@router.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: str):
    if not ObjectId.is_valid(item_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
    
    object_id = ObjectId(item_id)
    item = await Items.get(object_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return ItemResponse(id=str(item.id), name=item.name, description=item.description, price=item.price)

@router.get("/items/", response_model=ItemResponse)
async def get_item_by_name(name: str):
    item = await Items.find_one(Items.name == name)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return ItemResponse(id=str(item.id), name=item.name, description=item.description, price=item.price)

@router.put("/items/name/{item_name}", response_model=ItemResponse)
async def update_item_by_name(item_name: str, item: ItemCreate):
    # Find the item by name
    existing_item = await Items.find_one(Items.name == item_name)
    
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Update the fields
    existing_item.name = item.name
    existing_item.description = item.description
    existing_item.price = item.price
    await existing_item.save()  # Save the changes to the database
    
    return ItemResponse(id=str(existing_item.id), name=existing_item.name, description=existing_item.description, price=existing_item.price)

@router.delete("/items/name/{item_name}", response_model=dict)
async def delete_item_by_name(item_name: str):
    # Find the item by name
    item = await Items.find_one(Items.name == item_name)
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Delete the item
    await item.delete()
    return {"message": "Item deleted successfully"}
