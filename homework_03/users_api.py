from fastapi import APIRouter
from pydantic import constr

from schemas import UserIn, UserOut
from crud import create_user, list_users

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("")
def list_user():
    return list_users()


@router.post("", response_model=UserOut)
def create_users(user_in: UserIn):
    return create_user(user_in)
