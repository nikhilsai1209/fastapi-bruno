# restaurant_service/models.py

from beanie import Document
from pydantic import Field

class Restaurant(Document):
    name: str = Field(..., description="Name of the restaurant")
    location: str = Field(..., description="Location/address of the restaurant")

    class Settings:
        collection = "restaurants"

    class Config:
        schema_extra = {
            "example": {
                "name": "The Great Burger",
                "location": "123 Main Street, Springfield"
            }
        }
