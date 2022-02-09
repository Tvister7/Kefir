from pydantic import BaseModel, Field
from models.user import User


class LoginModel(BaseModel, User):
    email: str = Field(...)
    password: str = Field(...)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None

