from pydantic import BaseModel, Field, constr
from beanie import PydanticObjectId
from typing import Optional

class RestaurantCreate(BaseModel):
    name: constr(min_length=1, max_length=100) = Field(description="Name of the restaurant") # type: ignore
    location: constr(min_length=1, max_length=255) = Field(description="Location/address of the restaurant") # type: ignore

    class Config:
        schema_extra = {
            "example": {
                "name": "The Great Burger",
                "location": "123 Main Street, Springfield"
            }
        }

class RestaurantResponse(RestaurantCreate):
    id: PydanticObjectId

    class Config:
        orm_mode = True
        json_encoders = {PydanticObjectId: str}
        schema_extra = {
            "example": {
                "id": "64f5b2d0f29a4a6d33b20c73",
                "name": "The Great Burger",
                "location": "123 Main Street, Springfield"
            }
        }
