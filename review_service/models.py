from beanie import Document
from pydantic import EmailStr, constr, conint
import re

class Review(Document):
    email: EmailStr
    rating: conint(ge=0, le=5) # type: ignore
    comments: constr(min_length=1, max_length=1000) # type: ignore

    class Settings:
        collection = "reviews"

    @classmethod
    def validate_email_format(cls, email: str) -> str:
        # Regular expression to ensure the email follows the format username@domain.com
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise ValueError("Please enter a valid email address in the format username@domain.com")
        return email
