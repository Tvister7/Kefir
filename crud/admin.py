from email_validator import validate_email, EmailNotValidError
from fastapi import HTTPException
from models.user import User
from schemas.admin import PrivateDetailUserResponseModelPydantic, PrivateCreateUserModelPydantic


async def create_new_user(user: PrivateCreateUserModelPydantic) -> PrivateDetailUserResponseModelPydantic:
    try:
        validate_email(user.email)
    except EmailNotValidError as error:
        raise HTTPException(status_code=400, detail=str(error))
    user_obj = await User.create(**user.dict())
    await user_obj.save()
    if not user_obj:
        raise HTTPException(status_code=400, detail="Database error")
    return user_obj
