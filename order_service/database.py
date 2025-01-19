from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from order_service.models import Order  # Import your Order model
from user_service.models import User  # Ensure correct path
from restaurant_service.models import Restaurant  # Ensure correct path
from items_service.models import Item  # Ensure correct path

MONGO_URI = "mongodb+srv://nikhilthentu:r9w0u4OZDx2M4Eeh@cluster0.wgn3c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
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
