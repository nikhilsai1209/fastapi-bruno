from fastapi import APIRouter, HTTPException, status
from review_service.models import Review  # Your Beanie document for reviews
from review_service.schemas import ReviewCreate, ReviewResponse  # Your Pydantic models
from bson import ObjectId

router = APIRouter()

@router.post("/reviews/", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
async def create_review(review: ReviewCreate):
    # Create a new review from the incoming data
    new_review = Review(**review.dict())
    await new_review.insert()  # Save the new review to the database
    
    # Return the response model
    return ReviewResponse(id=str(new_review.id), **review.dict())

@router.get("/reviews/{review_id}", response_model=ReviewResponse)
async def get_review(review_id: str):
    if not ObjectId.is_valid(review_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
    
    object_id = ObjectId(review_id)
    
    # Retrieve the review by its ID
    review = await Review.get(object_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    # Return the review as a response model
    return ReviewResponse(id=str(review.id), order_id=review.order_id, rating=review.rating, comment=review.comment)

@router.put("/reviews/{review_id}", response_model=ReviewResponse)
async def update_review(review_id: str, review: ReviewCreate):
    if not ObjectId.is_valid(review_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
    
    object_id = ObjectId(review_id)
    existing_review = await Review.get(object_id)
    
    if not existing_review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    # Update the existing review with the new data
    existing_review.order_id = review.order_id
    existing_review.rating = review.rating
    existing_review.comment = review.comment
    await existing_review.save()  # Save the changes to the database
    
    return ReviewResponse(id=str(existing_review.id), order_id=existing_review.order_id, rating=existing_review.rating, comment=existing_review.comment)

@router.delete("/reviews/{review_id}", response_model=dict)
async def delete_review(review_id: str):
    if not ObjectId.is_valid(review_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
    
    object_id = ObjectId(review_id)
    result = await Review.get(object_id)
    
    if not result:
        raise HTTPException(status_code=404, detail="Review not found")
    
    await result.delete()
    return {"message": "Review deleted successfully"}
