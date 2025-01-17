from fastapi import FastAPI
from catalog_service.database import init_db
from catalog_service.routes import router as catalog_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()
    print("Catalog service started.")

@app.on_event("shutdown")
async def shutdown_event():
    print("Catalog service shutting down.")

app.include_router(catalog_router)
