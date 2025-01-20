from fastapi import FastAPI
from review_service.routes import router as review_router  # Import your review router
from order_service.routes import router as order_router    # Import your order router
from review_service.database import init_db  # Import the init_db function

app = FastAPI()

# Register your routers
app.include_router(review_router, prefix="/reviews", tags=["reviews"])
# app.include_router(order_router, prefix="/orders", tags=["orders"])

@app.on_event("startup")
async def on_startup():
    # Initialize the database connection
    await init_db()
