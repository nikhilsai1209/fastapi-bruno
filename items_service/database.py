from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from items_service.models import Item
from restaurant_service.models import Restaurant  # Ensure this model is available for validation

# MongoDB connection details (consider using environment variables in production)
MONGO_URI = "mongodb+srv://nikhilthentu:r9w0u4OZDx2M4Eeh@cluster0.wgn3c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "food_delivery"

async def init_db():
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        database = client[DB_NAME]
        await init_beanie(database, document_models=[Item, Restaurant])
        print("Items database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
