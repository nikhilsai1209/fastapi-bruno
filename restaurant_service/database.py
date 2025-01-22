from beanie import init_beanie
import os
from motor.motor_asyncio import AsyncIOMotorClient
from restaurant_service.models import Restaurant

# Hardcoded MongoDB connection details
MONGO_URI = "mongodb+srv://nikhilthentu:r9w0u4OZDx2M4Eeh@cluster0.wgn3c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "food_delivery"

async def init_db():
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        database = client[DB_NAME]
        await init_beanie(database, document_models=[Restaurant])
        print("Restaurant database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
