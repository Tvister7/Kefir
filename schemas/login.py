from pydantic import BaseModel, Field


class LoginModel(BaseModel):
    login: str = Field(...)
    password: str = Field(...)
