from fastapi import FastAPI
from restaurant_service.database import init_db
from restaurant_service.routes import router as restaurant_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()
    print("Restaurant service started.")

@app.on_event("shutdown")
async def shutdown_event():
    print("Restaurant service shutting down.")

app.include_router(restaurant_router, prefix="/api/v1", tags=["restaurants"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Restaurant Service API"}
