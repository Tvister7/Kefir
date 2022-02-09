from tortoise.contrib.pydantic import pydantic_model_creator
from models.user import User
from pydantic import BaseModel, Field

PrivateDetailUserResponseModelPydantic = pydantic_model_creator(User,
                                                                name="PrivateDetailUserResponseModel",
                                                                exclude=("password",))


class PrivateCreateUserModelPydantic(BaseModel, User):
    first_name: str = Field(...)
    last_name: str = Field(...)
    other_name: str
    email: str = Field(...)
    phone: str
    city: int
    birthday: str
    additional_info: str
    is_admin: bool = Field(...)
    password: str = Field(...)


PrivateUpdateUserModelPydantic = pydantic_model_creator(User,
                                                        name="PrivateUpdateUserModel",
                                                        exclude=("password",))
