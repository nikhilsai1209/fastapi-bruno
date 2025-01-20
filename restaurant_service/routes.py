from fastapi import APIRouter, HTTPException, status
from restaurant_service.models import Restaurant
from restaurant_service.schemas import RestaurantCreate, RestaurantResponse
from bson import ObjectId
from typing import List

router = APIRouter()

@router.post("/restaurants/", response_model=RestaurantResponse, status_code=status.HTTP_201_CREATED)
async def create_restaurant(restaurant: RestaurantCreate):
    new_restaurant = Restaurant(**restaurant.dict())
    await new_restaurant.insert()  # Save to the database
    return RestaurantResponse(id=str(new_restaurant.id), **restaurant.dict())

@router.get("/restaurants/{restaurant_id}", response_model=RestaurantResponse)
async def get_restaurant(restaurant_id: str):
    if not ObjectId.is_valid(restaurant_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId format")
    
    object_id = ObjectId(restaurant_id)
    restaurant = await Restaurant.get(object_id)
    if not restaurant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
    
    return RestaurantResponse(id=str(restaurant.id), name=restaurant.name, location=restaurant.location)

@router.get("/restaurants/", response_model=List[RestaurantResponse], status_code=status.HTTP_200_OK)
async def get_all_restaurants():
    """
    Get a list of all restaurants.
    """
    restaurants = await Restaurant.find_all().to_list()  # Fetch all restaurants from the database
    return [
        RestaurantResponse(id=str(restaurant.id), name=restaurant.name, location=restaurant.location) 
        for restaurant in restaurants
    ]
