from schemas import User, UserIn
from datetime import datetime


user_id: dict[int, User] = {}


def list_users() -> list[User]:
    return list(user_id.values())


def create_user(user_in: UserIn) -> User:
    new_id = len(user_id) + 1
    user = User(id=new_id, created_at=str(datetime.now()), **user_in.dict())
    user_id[new_id] = user
    return user
