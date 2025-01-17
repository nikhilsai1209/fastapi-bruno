# main.py
from fastapi import FastAPI
from review_service.routes import router as review_router
from review_service.database import initiate_db

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await initiate_db()  # Initialize database connection

app.include_router(review_router, prefix="/review")  # Include the review service router
