from pydantic import BaseModel, EmailStr, constr, conint, field_validator
import re

class ReviewCreate(BaseModel):
    email: EmailStr
    rating: conint(ge=0, le=5) # type: ignore
    comments: constr(min_length=1, max_length=1000) # type: ignore

    @field_validator('email')
    def validate_email_format(cls, value):
        # Regular expression to ensure the email follows the format username@domain.com
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise ValueError("Please enter a valid email address in the format username@domain.com")
        return value

class ReviewResponse(ReviewCreate):
    id: str

    class Config:
        orm_mode = True
