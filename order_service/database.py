from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from order_service.models import Order  # Import your Order model
from user_service.models import User  # Ensure correct path
from restaurant_service.models import Restaurant  # Ensure correct path
from items_service.models import Item  # Ensure correct path
import os
from dotenv import load_dotenv 
load_dotenv()


MONGO_URI = os.getenv("DB_CONNECTION_STRING") 
DB_NAME = "food_delivery"

async def init_db():
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        database = client[DB_NAME]
        await init_beanie(database, document_models=[Order, User, Restaurant, Item])
        print("Order service database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
