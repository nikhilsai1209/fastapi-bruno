from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from catalog_service.models import Items
import os
from dotenv import load_dotenv 
load_dotenv()

# Hardcoded MongoDB connection details
MONGO_URI = os.getenv("DB_CONNECTION_STRING") 
  # Replace with your MongoDB URI
DB_NAME = "food_Db"                    # Replace with your database name

async def init_db():
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        database = client[DB_NAME]
        await init_beanie(database, document_models=[Items])
        print("Catalog database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
