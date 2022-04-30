from pydantic import BaseModel, constr


class UserBase(BaseModel):
    username: constr(min_length=8)
    email: str = "default@default"


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int
    created_at: str


class User(UserOut):
    pass
