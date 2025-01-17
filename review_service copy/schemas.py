from pydantic import BaseModel

class ReviewCreate(BaseModel):
    order_id: str  # ID of the order being reviewed
    rating: int  # Rating for the order
    comment: str  # Comment for the review

class ReviewResponse(BaseModel):
    id: str  # ID of the review
    order_id: str  # ID of the order being reviewed
    rating: int  # Rating for the order
    comment: str  # Comment for the review

    class Config:
        orm_mode = True  # Enable ORM mode for response serialization
