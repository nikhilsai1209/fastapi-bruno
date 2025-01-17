from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    name: str

class UserResponse(UserCreate):
    id: str

    class Config:
        orm_mode = True
