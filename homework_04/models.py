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
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    relationship,
)

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)
import asyncpg

PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost/postgres"
)


# PG_CONN_URI = "postgresql+asyncpg://hw4:hw4@localhost:5432/hw4"

async_engine = create_async_engine(url=PG_CONN_URI)
Session: AsyncSession = sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession
)

# Session = scoped_session(async_session)
# session: AsyncSession = Session()

# async def create_engine():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)


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


Base = declarative_base(bind=async_engine, cls=Base)


class User(Base):
    __tablename__ = "User"
    name = Column("name", String)
    username = Column("username", String, unique=True)
    email = Column("email", String, unique=True)
    post_rlt = relationship("Post", back_populates="user_rlt")


class Post(Base):
    __tablename__ = "Post"
    user_id = Column("user_id", Integer, ForeignKey("User.id"))
    title = Column("title", String)
    body = Column("body", String)
    user_rlt = relationship("User", back_populates="post_rlt")


def create_table():
    Base.metadata.create_all()

async def create_user(name: str, username: str, email: str) -> User:
    async with Session() as session:
        username = User(username=username, name=name, email=email)
        session.add(username)
        await session.commit()
        await session.refresh(username)
    return username

async def create_post(user_id: int, title: str, body: str) -> Post:
    async with Session() as session:
        post = Post(user_id=user_id, title=title, body=body)
        session.add(post)
        await session.commit()
        await session.refresh(post)
    return post




# async def create_session() -> AsyncSession:
#     async with session_factory() as session:
#         return session