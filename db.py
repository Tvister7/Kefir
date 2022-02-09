import os
from dotenv import load_dotenv
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

load_dotenv(".env")
TORTOISE_DATABASE_URL = os.environ["DATABASE_URL"]

TORTOISE_ORM = {
    "connections": {"default": TORTOISE_DATABASE_URL},
    "apps": {
        "models": {
            "models": ["models.tasks", "models.users", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=TORTOISE_DATABASE_URL,
        modules={"models": ["models.city", "models.user"]},
        generate_schemas=True,
        add_exception_handlers=True
    )