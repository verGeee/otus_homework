"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import (
    Table,
    create_engine,
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    Session as SessionType,
)

# PG_CONN_URI = (
#     os.environ.get("SQLALCHEMY_PG_CONN_URI")
#     or "postgresql+asyncpg://postgres:password@localhost/postgres"
# )


PG_CONN_URI = "postgresql+pg8000://hw4:hw4@localhost:5432/hw4"

engine = create_engine(url=PG_CONN_URI)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Base:
    id = Column(Integer, primary_key=True)
    def __str__(self):
        return (
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"name={self.name!r}, "
            f"email={self.email!r} "
        )

    def __repr__(self):
        return str(self)


Base = declarative_base(bind=engine, cls=Base)


class User(Base):
    __tablename__ = "User"
    name = Column("name", String)
    username = Column("username", String, unique=True)
    email = Column("email", String, unique=True)

class Post(Base):
    __tablename__ = "Post"
    user_id = Column("user_id", Integer, unique=True)
    title = Column("title", String)
    body = Column("body", String)


def create_table():
    Base.metadata.create_all()

# def get_users(session: SessionType) -> list[User]:
#     users = session.query(User).all()
#     print("users:", users)
#     return users


# def create_user(session: SessionType, username: str, name: str, email: str) -> User:
#     username = User(username=username, name=name, email=email)
#     session.add(username)
#     session.commit()
#     return username


# def change_user(session: SessionType, user: User) -> User:
#     user.email = "new_email"
#     session.commit()
#     return user

session: SessionType = Session()
# create_table()
# get_users(session)
# create_user(session, username="vergee", name="pash", email="verge@email.com")
# change_user(session, username='test', name='test_name', email='test_email')
session.close()


