from fastapi import FastAPI
from pydantic import constr

from router_api import router as items_router
from users_api import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
async def root():
    return {"msg": "homework_03"}


@app.get("/ping/")
async def ping():
    return {"message": "pong"}
