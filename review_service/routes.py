from fastapi import APIRouter, HTTPException, status
from review_service.models import Review
from review_service.schemas import ReviewCreate, ReviewResponse
from bson import ObjectId

router = APIRouter()

@router.post("/reviews/", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
async def create_review(review: ReviewCreate):
    # Validate email format
    Review.validate_email_format(review.email)
    
    new_review = Review(**review.dict())
    await new_review.insert()  # Save to the database
    return ReviewResponse(id=str(new_review.id), **review.dict())

@router.get("/reviews/{review_id}", response_model=ReviewResponse)
async def get_review(review_id: str):
    if not ObjectId.is_valid(review_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
    
    object_id = ObjectId(review_id)
    
    review = await Review.get(object_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    return ReviewResponse(id=str(review.id), email=review.email, rating=review.rating, comments=review.comments)

@router.put("/reviews/{review_id}", response_model=ReviewResponse)
async def update_review(review_id: str, review: ReviewCreate):
    if not ObjectId.is_valid(review_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
    
    object_id = ObjectId(review_id)
    existing_review = await Review.get(object_id)
    
    if not existing_review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    # Validate email format
    Review.validate_email_format(review.email)
    
    existing_review.email = review.email
    existing_review.rating = review.rating
    existing_review.comments = review.comments
    await existing_review.save()  # Save the changes to the database
    
    return ReviewResponse(id=str(existing_review.id), email=existing_review.email, rating=existing_review.rating, comments=existing_review.comments)

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
