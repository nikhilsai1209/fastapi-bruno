from fastapi import FastAPI
from .database import init_db
from .routes import router as order_router

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(order_router, prefix="/api/v1", tags=["orders"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Order Service"}
