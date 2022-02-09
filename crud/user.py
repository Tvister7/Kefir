import os
from typing import Union
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError

from models.user import User
from schemas.login import LoginModel
from schemas.user import CurrentUserResponseModelPydantic
from utils.auth import oauth2_scheme
from utils.authfunc import verify_password


SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = os.environ["ALGORITHM"]


async def get_by_email_for_login(email: str) -> LoginModel:
    return await LoginModel.from_queryset_single(User.get(email=email))


async def get_by_email(email: str) -> CurrentUserResponseModelPydantic:
    return await CurrentUserResponseModelPydantic.from_queryset_single(User.get(email=email))


async def authenticate_user(login: LoginModel) -> Union[LoginModel, bool]:
    user_obj = await get_by_email_for_login(login.email)
    if not user_obj:
        return False
    if not verify_password(login.password, user_obj.dict().get('password')):
        return False
    return user_obj


async def get_current_user(token: str = Depends(oauth2_scheme)) -> CurrentUserResponseModelPydantic:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = await get_by_email(email=payload.get('email'))
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )
    return user


async def get_current_active_user(current_user: CurrentUserResponseModelPydantic = Depends(get_current_user))\
        -> CurrentUserResponseModelPydantic:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
