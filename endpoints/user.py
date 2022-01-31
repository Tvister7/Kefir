from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
async def user_get():
    return {"msg": "Hello, mate"}


@router.get("/current")
async def current_user_users_current_get():
    pass


@router.get("/")
async def users_users_get():
    pass


@router.get("/{pk}")
async def users_users_get(pk: int):
    pass


@router.get("/{pk}")
async def edit_user_users__pk__patch():
    pass
