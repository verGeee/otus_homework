from pydantic import BaseModel, constr


class UserBase(BaseModel):
    username: constr(min_length=8)


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int
    created_at: str

class User(UserOut):
    pass
