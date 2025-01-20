from fastapi import FastAPI
from items_service.database import init_db
from items_service.routes import router as item_router  # Import your router

app = FastAPI(title="Item Service", description="Service for managing menu items for restaurants")

@app.on_event("startup")
async def start_db():
    await init_db()
    print("Item service database initialized.")

@app.on_event("shutdown")
async def shutdown():
    print("Shutting down Item service...")

# Include your router
app.include_router(item_router)

# Optionally, you can define root endpoint
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Item Service API"}
