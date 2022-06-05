from fastapi import APIRouter
from pydantic import constr

router = APIRouter(tags=["Items"], prefix="/items")


@router.get("/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


@router.get("/hello")
def hello_view(name: constr(min_length=3) = "Not input"):
    return {"msg": f"Hello {name}"}


@router.get("/add")
def get_summ(a: int = 1, b: int = 5):
    return {f"Summ {a} and {b} is {a+b}"}


@router.post("")
def create_item(data: dict):
    return {"data": data}
