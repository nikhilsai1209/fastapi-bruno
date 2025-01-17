from beanie import Document

class User(Document):
    email: str
    name: str

    class Settings:
        collection = "users"
