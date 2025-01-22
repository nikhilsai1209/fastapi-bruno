# review_service/db.py
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from review_service.models import Review  # Import your Beanie model
import os

async def initiate_db():
    client = AsyncIOMotorClient("mongodb+srv://nikhilthentu:r9w0u4OZDx2M4Eeh@cluster0.wgn3c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Replace with your MongoDB Atlas URI
    database = client.get_database("food_Db")   # Replace with your database name
    await init_beanie(database, document_models=[Review])  # Initialize Beanie with your models
