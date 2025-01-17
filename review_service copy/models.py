from beanie import Document
from pydantic import conint, constr

class Review(Document):
    order_id: str  # ID of the order being reviewed
    rating: conint(ge=0, le=5)  # Rating for the order, ensuring it is between 0 and 5
    comment: constr(min_length=1, max_length=1000)  # Optional comment with a max length of 1000

    class Settings:
        collection = "reviews"  # The MongoDB collection name for reviews
