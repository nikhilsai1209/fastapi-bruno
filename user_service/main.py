from fastapi import FastAPI
from user_service.database import init_db
from user_service.routes import router as user_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()
    print("User service started.")

@app.on_event("shutdown")
async def shutdown_event():
    print("User service shutting down.")

app.include_router(user_router)
