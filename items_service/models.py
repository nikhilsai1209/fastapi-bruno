# items_service/models.py

from beanie import Document
from pydantic import Field
from bson import ObjectId

class PydanticObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return ObjectId(value)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema: dict) -> dict:
        schema.update(type='string', pattern='^[0-9a-f]{24}$')
        return schema

class Item(Document):
    name: str
    description: str
    price: int
    restaurant_id: PydanticObjectId  # Use PydanticObjectId

    class Settings:
        collection = "items"

    class Config:
        schema_extra = {
            "example": {
                "name": "Pizza",
                "description": "Delicious cheese pizza",
                "price": 10,
                "restaurant_id": "64f5b2d0f29a4a6d33b20c71"
            }
        }
