from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/login")
async def login_login_post():
    pass


@router.get("/logout")
async def logout_logout_get():
    pass
