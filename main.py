import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from db import init_db
from endpoints import user, admin, login

app = FastAPI(title="Kefir")


@app.on_event("startup")
async def startup_event():
    init_db(app)


app.include_router(user.router, prefix="/users", tags=["user"])
app.include_router(admin.router, prefix="/private", tags=["admin"])
app.include_router(login.router, tags=["auth"])

load_dotenv(".env")
HOST = os.environ["UVICORN_HOST"]
PORT = int(os.environ["UVICORN_PORT"])

# add_pagination(app)

if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, host=HOST, reload=True)
