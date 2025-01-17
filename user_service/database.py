from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from user_service.models import User

# Hardcoded MongoDB connection details
MONGO_URI = "mongodb+srv://nikhilthentu:r9w0u4OZDx2M4Eeh@cluster0.wgn3c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
  # Replace with your MongoDB URI
DB_NAME = "food_delivery"                   # Replace with your database name

async def init_db():
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        database = client[DB_NAME]
        await init_beanie(database, document_models=[User])
        print("User database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
