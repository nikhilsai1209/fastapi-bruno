from fastapi import APIRouter, HTTPException, status
from user_service.models import User
from user_service.schemas import UserCreate, UserResponse

router = APIRouter()

@router.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    existing_user = await User.find_one({"email": user.email})
    
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists.")
    
    new_user = User(**user.dict())
    await new_user.insert()  # Insert new user into the database
    
    return UserResponse(id=str(new_user.id), email=new_user.email, name=new_user.name)

@router.get("/users/{email}", response_model=UserResponse)
async def get_user_by_email(email: str):
    user = await User.find_one({"email": email})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    return UserResponse(id=str(user.id), email=user.email, name=user.name)

@router.get("/users/validate/{email}", response_model=dict)
async def validate_user(email: str):
    user = await User.find_one({"email": email})
    
    if not user:
        return {"valid": False, "message": "User not found."}
    
    return {"valid": True, "message": "User is valid."}
