from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    price: int

class ItemResponse(ItemCreate):
    id: str

    class Config:
        orm_mode = True
