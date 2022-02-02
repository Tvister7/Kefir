from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from models.user import User

CurrentUserResponseModelPydantic = pydantic_model_creator(User,
                                                          name="CurrentUserResponseModel",
                                                          exclude=("city", "additional_info", "password"),
                                                          exclude_readonly=True)

UpdateUserModelPydantic = pydantic_model_creator(User,
                                                 name="UpdateUserModel",
                                                 exclude_readonly=True,
                                                 exclude=("city", "password", "is_admin", "additional_info"))

UpdateUserResponseModelPydantic = pydantic_model_creator(User,
                                                         name="UpdateUserResponseModel",
                                                         exclude=("city", "password", "is_admin", "additional_info"))

UsersListElementModelPydantic = pydantic_queryset_creator(User,
                                                          name="UsersListElementModel",
                                                          exclude=("city", "password", "is_admin", "additional_info",
                                                                   "other_name", "birthday", "phone"))
