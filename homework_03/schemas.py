from pydantic import BaseModel, constr


class UserBase(BaseModel):
    username: constr(min_length=8)


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int


class User(UserOut):
    # token: str
    pass
