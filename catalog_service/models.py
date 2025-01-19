from beanie import Document

class Items(Document):
    name: str
    description: str
    price: int

    class Settings:
        collection = "catalog"
