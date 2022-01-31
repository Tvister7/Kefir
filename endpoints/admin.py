from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def private_users_private_users_get():
    return {"msg": "Hello, mate"}


@router.post("/users")
async def private_create_users_private_users_post():
    pass


@router.get("/users/{pk}")
async def private_get_user_private_users__pk__get():
    pass


@router.delete("/users/{pk}")
async def private_delete_user_private_users__pk__delete():
    pass


@router.patch("/users/{pk}")
async def private_patch_user_private_users__pk__patch():
    pass

